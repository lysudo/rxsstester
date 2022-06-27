#!/bin/python3

import requests,sys
from urllib.parse import urlparse

#suppress warnings
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

args = sys.argv

if len(args) < 3:
	print(f"please provide target urls and params files ..\nUSAGE: {args[0]} <urls> <params>")
	exit()

if args[1] == "-url" :
	url = args[2]
	try:
		with open(args[3],'r') as params:
				for param in params:
					r = requests.get(url,params={param:"FUZZ"},verfiy=False)
					if "FUZZ" in r.text :
						print(f"[+] {url} ######>>>>###### {param}") 
	except IndexError:
		print(f"params file not privded ..\nUSAGE: {args[0]} <urls> <params>")
		exit()
	exit()

with open(args[1],'r') as urls:
	for url in urls:
		url = urlparse(url).path
		with open(args[2],'r') as params:
			for param in params:
				try:
					r = requests.get(url,params={param:"FUZZ"},verify=False)
					if "FUZZ" in r.text :
						print(f"[+] {url} ######>>>>###### {param}") 
				except:
					pass
