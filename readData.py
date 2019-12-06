from matplotlib.pyplot import plot

data = {}

for name in ['abdomen1', 'abdomen2', 'abdomen3', 'thorax1', 'thorax2']:
	with open(name + '.txt') as f:
		data[name] = [ float(x) for x in f.readlines() ]

print('data read')

plot(range(0, len(data['abdomen1'])), data['abdomen1'])
