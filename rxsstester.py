#!/bin/python3

import requests,sys
import re,sys,getopt
from urllib.parse import urlparse
from os.path import exists


######## suppress urllib warnings
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
########

def message(notfound="", required=""):
	
	#ERROR MESSAGES
	if notfound:
		print(f"<{notfound}> file not found ..")

	if required:
		print(f"<{required}> file is (required) ..")


	#USAGE MESSAGE
	print(f"""\nusage: {__file__} -f <inputfile>

	OPTIONS: 
	-f / --targetsfile <file> : line separated file contains target endpoits
	--url : a singl endpoint to test against
	-p / --paramsfile <file> : line separated file contains list of parameters to test
	-o <outputfile> ,write to specific file 
	--silent : sshh ,don't show results""")

#in case no argv privded
if len(sys.argv) < 2:
		print("please provide args ..")
		message()
		exit()

def fuzz(target ,paramsfile,output ,isFile=True,write=False ,silent=False):
	targets = []
	params = []
	results = []

	#######################
	#if it's a single URL '--url'
	if not isFile:
		targets.append(urlparse(target).path)
		try:	
			with open(paramsfile, 'r',encoding="utf-8") as p:
				params = list(p)
		except FileNotFoundError:
			message(required="")
			exit()

	#if it's a file '-f'
	else:
		try:
			with open(target, 'r',encoding="utf-8") as t:
				targets = list(t)
		except FileNotFoundError:
			message(required="target")
			exit()

		try:	
			with open(paramsfile, 'r',encoding="utf-8") as p:
				params = list(p)
		except FileNotFoundError:
			message(required="params")
			exit()
	########################
	
	for url in targets:
		url = urlparse(url)
		url = url.scheme+"://"+url.netloc+url.path if isFile else target
		if not silent:
			print(f"[!] testing for {url}")

		# the whole thing ..
		for param in params:
			try:
				r = requests.get( url ,params={param:"FUZZ"},verify=False)
			except requests.exceptions.ConnectionError:
				print("[X] please check your connection ..")
				exit()
			except requests.exceptions.InvalidSchema:
				print("[X] InvalidSchema: please check if the url have the proper schema [http/https]")
				exit()

			if "FUZZ" in r.text and param not in results:
				results.append("%s => %s\n-----"% (url,param))
				if not silent:
					print(f"[+] => {param}")

	if write and results:
		with open(output,'w',encoding="utf-8") as o:
			for result in results:
				o.write(result)

def main(argv):

	try:
		opts,values = getopt.getopt(argv,"hf:p:o:",["targetsfile=","paramsfile=","url=","silent"])
	
	except getopt.GetoptError:
		message()
		exit()

	try:
		if opts[0][0] == '-h':
			message()
			exit()

	except IndexError:
		message()

	#settings
	target = ""
	paramsfile = ""
	output = "rxssresults.txt" #default
	isFile = True #whether it's a file '-f' or single url '--url'
	write = False
	silent = False

	
	for key,value in opts:

		if key == "-f" or key == "--targetfile":
			if not exists(value):
				message(notfound="target")
				exit()
			target = value

		elif key == "--url":
			target = value
			isFile = False

		elif key == "-p" or key == "--paramsfile":
			if not exists(value):
				messag(notfound="params")
				exit()
			paramsfile = value


		elif key == "-o":
			output = value
			write = True

		elif key == "--silent":
			silent = True


	fuzz(target,paramsfile,output,isFile=isFile,write=write,silent=silent)


if __name__ == "__main__":
	main(sys.argv[1:])