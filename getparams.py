#!/bin/python3

import re
import sys
import getopt
from urllib.parse import urlparse
from os.path import exists

def message():
	print(f"""
usage: {__file__} [OPTIONS]
OPTIONS: 
	-f <targetfile> ,contains line separated urls/endpoits
	-o <outputfile> ,write to specific file 
	--silent ,don't show results""")


#in case no argv privded
if len(sys.argv) < 2:
		print("please provide args ..")
		message()
		exit()


def main(argv):

	try:
		opts,values = getopt.getopt(argv,"hf:o:",["silent"])
	except getopt.GetoptError:
		message()
		exit()

	try:
		if opts[0][0] == '-h':
			message()
			exit()
	except IndexError:
		print(f"usage: {__file__} -f <inputfile>")
	
	#settings
	inputfile = ""
	outputfile = ""
	silent = False

	#set settings
	for key,value in opts:
		if key == '-f':
			inputfile = value
		elif key == '-o':
			outputfile = value
		elif key == "--silent":
			silent = True

	if not exists(inputfile):
		print(f'file "{inputfile}" not exist ..')
		exit()
	
	#READ WRITE FILES
	with open(inputfile, 'r',encoding="utf-8") as i:
		
		results = []
		for line in i:
			url = urlparse(f"{line}")._replace(fragment="").geturl()
			regex = r"(?:\?|\&)(?P<key>[\w]+)=(?P<value>[\w+,.-.%]+)(?:\:?)(?P<option>[\w,]*)"
			params = re.findall(regex,url)

			for match in params:
				if match[0] not in results:
					results.append(match[0])
					if not silent:
						print(match[0])

		# if user specified file
		if outputfile:
			with open(outputfile,'w',encoding="utf-8") as o:
				for result in results:
					o.write(f"{result}\n")

if __name__ == "__main__":
	main(sys.argv[1:])



