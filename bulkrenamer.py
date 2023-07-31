import os
import sys
import argparse

def main():

	i=1
	path = "/Users/f1fth/Desktop/fotosort/"
	for filename in os.listdir(path):
		target = sys.argv[1] + "-" + filename
		source = path + filename
		target = path + target
		os.rename(source, target)
		i += 1
		print (target)
		print (source)
		print (filename)


if __name__ == '__main__':
	main()
