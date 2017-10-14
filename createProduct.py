#!/usr/bin/python
"""
This is an example of how to build a product creator
"""

import sys, getopt
import MySQLdb
from includes import DB as DB
from includes import Checker as Checker
from includes import Creator as Creator
from includes import Table as Table

def main():

	print "############################################################"
	print "This assistant will take you through the process of creating"
	print "a product by Category. Enjoy the first beta ;)"
	print "############################################################\n"

	a = 1
	while a == 1:
		try:
			username = raw_input("--->Enter a valid username to begin: ")
		except EOFError as e:
			print "%s problem with username" % e

		if(Checker.check_availability(username, "users", "username") == "True"):
			# Keep asking for product details
			# Category
			try:
				product_id = raw_input("--->Enter product_id: ")
				product_category = raw_input("--->Enter the category of the product: ")
				price = raw_input("--->Enter your desired price: ")
				owner_id = username
				neighborhood_id = raw_input("--->Enter neighborhood_id: ")
				address1 = raw_input("--->Enter your address: ")
			except EOFError as e:
				print "%s problem with category" % e
			
			d = {"product_id" : product_id,
				"product_category" : product_category,
				"price" : price,
				"owner_id" : owner_id,
				"neighborhood_id" : neighborhood_id,
				"address1" : address1}
			t = Table(d)

			# Creating the product in the DB
			creator = Creator()
			creator.createProduct(t)

			# Asking before quitting
			try:
				resp = raw_input("Would you like to add another product? [Y/n]: ")
			except EOFError as e:
				print "Quitting."
				a = 0
			if str(resp) == "n":
				a = 0
		else:
			print "User %s is not registered. Retrying..." % username







if __name__=="__main__":
	main()