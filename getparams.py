#!/bin/python3
import re,sys
from urllib.parse import urlparse

args = sys.argv
if len(args) < 2:
	print("target file not provided ..")
	exit()

with open(args[1]) as file:
	results = []
	for line in file:

		url = urlparse(f"{line}")._replace(fragment="").geturl()
		params = re.findall(r"(?:\?|\&)(?P<key>[\w]+)=(?P<value>[\w+,.-.%]+)(?:\:?)(?P<option>[\w,]*)",url)

		for match in params:
		
			if match[0] not in results:
				results.append(match[0])
				print(match[0])
