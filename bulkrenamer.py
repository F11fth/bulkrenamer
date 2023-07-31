import os
import sys
import argparse
import datetime

def main():
	
	timestamp = datetime.datetime.now()
	date = timestamp.date().isoformat()
	path = "/Users/f1fth/Desktop/fotosort/"
	for filename in os.listdir(path):
		target = date + "-" + filename
		source = path + filename
		target = path + target
		os.rename(source, target)

if __name__ == '__main__':
	main()
