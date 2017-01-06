from argparse import ArgumentParser
from graph import Greengraph
from matplotlib import pyplot as plt

#%matplotlib qt

def process():
	parser = ArgumentParser(description = "Green counts between two locations")
	
	parser.add_argument('--origin', '-o')
	parser.add_argument('--destination','-d')
	parser.add_argument('--steps', '-s')
	parser.add_argument('--out', '-f')
	arguments= parser.parse_args()
	greenGraphObject = Greengraph(arguments.origin,arguments.destination)
	data = greenGraphObject.green_between(arguments.steps)
	plt.plot(data)
	plt.show()

if __name__ == "__main__":
	process()
