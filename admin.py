#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError,URLError


class admin:

	def __init__(self,link):

		f = open("link.txt","r");
		print ("\n\nAvilable links : \n")
		while True:
			sub_link = f.readline()
			if not sub_link:
				break
			req_link = "http://"+link+"/"+sub_link
			try:
				response = urlopen(req_link)
			except HTTPError as e:
				continue
			except URLError as e:
				continue
			else:
				print ("OK => ",req_link)
