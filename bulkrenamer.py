import os
import sys
import datetime

def main():
	
	timestamp = datetime.datetime.now()
	date = timestamp.date().isoformat()
	#ToDo: Compress
	
	path = sys.argv[1]
	stocktype = sys.argv[2]
	stocknumber = sys.argv[3]
	#ToDo: add argparse
	for filename in os.listdir(path):
		target = date + "-" + stocktype + "-" + stocknumber + "-" + filename
		source = path + filename
		target = path + target
		os.rename(source, target)

if __name__ == '__main__':
	main()
