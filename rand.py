
import sys, string, os
import subprocess 


STAT = True
if STAT:
	STAT_F = open('stat.txt', 'a')



def isInt(value):
  try:
    int(value)
    return True
  except:
    return False


def shift(stroka, count):
	x = 0
	while x < count:
		tmp = stroka[-1]
		stroka = tmp + stroka[:-1]
		x += 1 
	return stroka



class Scan:
	"""docstring for Scan"""
	def __init__(self, file, count):
		self.file = file
		self.count = count
		str_bin = ''
		with open(file, "rb") as f:
		    byte = f.read(1)
		    while byte != "":
		        str_bin += ''.join(format(ord(x), 'b') for x in byte)
		        byte = f.read(1)
		self.str_bin = str_bin
		self.lenstr = len(str_bin)
		size = self.lenstr / self.count
		arr = []
		x = 0
		tmp = 0
		for char in self.str_bin[:size*count]:
			x += 1
			if x < size:
				tmp += int(char)
			elif x == size: 
				tmp += int(char)
				x = 0
				arr.append(tmp)

		self.arr = arr

	def random_str(self):
		output = ''
		for item in self.arr:
			output += string.printable[item % 94]	
		print output
		if STAT:
			STAT_F.write(output + '\n')

	def random_int(self):
		output = ''
		# print self.arr 
		for item in self.arr:
			itemstr = str(item)
			while itemstr.find("00") != -1:
				itemstr = itemstr.replace("00","0")
			while len(itemstr) > 1:
				item = int(itemstr[0])
				itemstr = shift(itemstr[1:],item)
			output += itemstr
		if STAT:
			STAT_F.write(output + '\n')
		print output
		



def main():
	file  = "FMcapture.dat"


	bashCommand = "rtl_sdr -f 25835000 -g 0 -s 1000000 -n 10000 " + file
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
	if not os.path.isfile("FMcapture.dat"):
		print "Does not exist temp file"
		sys.exit()
	go = True
	if sys.argv[1]:
		inpu = sys.argv[1]
		if not (inpu[-1] == "s" or inpu[-1] == "d") and not isInt(inpu[:-1]):
			pass
		else:
			rc = int(inpu[:-1])
			if inpu[-1] == "s":
				rw = 'string'
			else: 
				rw = 'digits'
			go = False

	if go:
		rc = raw_input("\nCount of symbols?\n")
		while not isInt(rc):
			rc = raw_input("Count of symbols?\n")

	sc = Scan(file, int(rc))	
	
	# print "\nAll chars: " + sc.lenstr + "\n"

	if go:
		rw = raw_input("String or digits?\n")
		while not (rw == "string" or rw == "digits"):
			rw = raw_input("String or digits?\n")

	print "------------------------------\n"
	if rw == "string":
		sc.random_str()
	else:
		sc.random_int()



if __name__ == "__main__":
	main()
	if STAT:
		STAT_F.close()
	sys.exit()
