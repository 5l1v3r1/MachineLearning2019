import matplotlib.pyplot as plt

files = ['abdomen1', 'abdomen2', 'abdomen3', 'thorax1', 'thorax2']


def add_plot(data: [float], max_len: int, ax: plt.Axes):
    ax.plot(range(min(max_len, len(data))), data[:min(len(data), max_len)])


def plot_data(data: [[float]]):
    f, ax = plt.subplots(len(files))
    for i, name in zip(range(len(files)), files):
        add_plot(data[i], 2000, ax[i])
    plt.show()


def read_data(file_name: str):
    with open(file_name + '.txt') as f:
        return [float(x) for x in f.readlines()]


if __name__ == '__main__':
    data = [read_data(file_name) for file_name in files]

    # Plot given data
    plot_data(data)

    # Wavelet transform

    # Plot Transformed data

    # Transform back

    # Plot output data
