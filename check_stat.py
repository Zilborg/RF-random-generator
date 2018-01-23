import sys 
import numpy 
import seaborn as sns
import matplotlib.pyplot as plt

# FILE = sys.argv[1]

def main():
	arr = []
	with open('stat.txt', 'r') as STAT_F:
		for line in STAT_F:
			arr.append(line[:-1])

	arr_stat = []
	stat = {}
	for item in range(10):
		stat.update({str(item):0})
	for item in range(len(arr[0])):
		arr_stat.append(stat)

	for item in arr:
		for it in range(len(item)):
			arr_stat[it][item[it]] += 1
	# print arr_stat

	arr = map(int, arr)
	numpy.random.seed(0)
	arr2 = numpy.random.randint(0,100, 1000)

	plt.xlim((-1,100))
	plt.ylim((0,30))
	plt.hist(arr2, bins = 99)
	plt.savefig('np.pdf')
	plt.show()
 	plt.hist(arr, bins = 99 )
 	plt.xlim((-1,100))
	plt.ylim((0,30))
 	plt.savefig('my.pdf')
 	plt.show()


if __name__ == "__main__":
	main()
	sys.exit()