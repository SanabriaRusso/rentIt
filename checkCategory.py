#!/usr/bin/python
"""
This is an example of how to build checks for any product category
"""

import sys, getopt
import MySQLdb
from includes import DB as DB
from includes import Checker as Checker

def main():

	while 1:
		category = ""
		try:
			category = raw_input("Please enter product category: ")
		except EOFError as e:
			print "%s problem with category" % e

		if (Checker.check_availability(category, "products", "product_category") == "True"):
			print "Product \"%s\" found" % category
		else:
			print "No matches for category: %s. Would you like to create it?" % category



if __name__=="__main__":
	main()