from matplotlib.pyplot import plot, show

def plot_data(data: [float], max_len: int):
    plot(range((min(max_len, len(data))), data[:min(len(data), max_len)])
    show()

def read_data(name: str):
    with open(name + '.txt') as f:
        return [float(x) for x in f.readlines()]

if __name__ == '__main__':
    for name in ['abdomen1', 'abdomen2', 'abdomen3', 'thorax1', 'thorax2']:
        plot_data(read_data(name), 2000)