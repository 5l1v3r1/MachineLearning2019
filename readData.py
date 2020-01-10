import matplotlib.pyplot as plt
import pywt

files = ['abdomen1', 'abdomen2', 'abdomen3', 'thorax1', 'thorax2']


# Data I/O
def read_data(file_name: str):
    with open(file_name + '.txt') as f:
        return [float(x) for x in f.readlines()]


# Plotting
def add_plot(data: [float], max_len: int, ax: plt.Axes):
    ax.plot(range(min(max_len, len(data))), data[:min(len(data), max_len)])


def plot_data(data: [[float]], title: str = ''):
    f, ax = plt.subplots(len(files))
    f.suptitle(title)
    plt.subplots_adjust(hspace=1)
    for i, name in zip(range(len(files)), files):
        add_plot(data[i], 2000, ax[i])
        ax[i].set_title(name)
    plt.draw()
    print('Drawn plot:', title)


def plot_single_data(data: [float], title: str = ''):
    plt.figure()
    plt.plot(list(range(2000)), data[:2000])
    plt.draw()
    print('Drawn plot:', title)


# Normalize input data
def normalize_data(data):
    mean = sum(data) / len(data)
    data = [d - mean for d in data]
    m = max(data)
    return [d / m for d in data]


# Wavelet transform
def wavelet(data: [float], style: str = 'haar'):
    a, d = pywt.dwt(data, style)
    return a, d


def inverse_wavelet(data: [float], detail: [float] = None, style: str = 'haar'):
    return pywt.idwt(cA=data, cD=detail, wavelet=style)


def stationary_wavelet(data: [float], style: str = 'haar'):
    l = pywt.swt(data, style)
    al, dl = [], []
    for a, d in l:
        al.append(a)
        dl.append(d)
    return a, d


def inverse_stationary_wavelet(data: [float], detail: [float] = [], style: str = 'haar'):
    print('a', data)
    if len(detail) == 0:
        detail = [[0 for _ in wave] for wave in data]
    print('d', detail)
    print(len(detail))
    return pywt.iswt(coeffs=list(zip(data, detail)), wavelet=style)


if __name__ == '__main__':
    data = [read_data(file_name) for file_name in files]

    # Plot given data
    plot_data(data, 'Given data')

    # Normalize data
    data = [normalize_data(d) for d in data]
    plot_data(data, 'Normalized data')

    # Wavelet transform
    # w_style = 'haar'
    w_style = 'bior1.1'
    # w_style = 'db1'

    data = [stationary_wavelet(d, w_style) for d in data]
    # data = [([], [])]

    # Plot Transformed data
    plot_data([x for x, _ in data], 'Wavelet ({}) adjusted data'.format(w_style))
    plot_data([x for _, x in data], 'Wavelet detail data')

    # Transform back
    with_detail = inverse_stationary_wavelet([d for d, _ in data], [d for _, d in data], style=w_style)
    without_detail = inverse_stationary_wavelet([d for d, _ in data], style=w_style)
    print(with_detail)
    # Plot output data
    plot_single_data(with_detail, title='Re-transformed data ({}, with detail)'.format(w_style))
    plot_single_data(without_detail, title='Re-transformed data ({}, without detail)'.format(w_style))
    # plot_data([a - b for a, b in zip(with_detail, without_detail)],
    #           title='Difference re-transforms with/without detail')

    plt.show()
