#!/usr/bin/python
import sys, getopt
import MySQLdb
from includes import DB as DB
MARCODB = "192.168.167.116"
MARCOUSER = "dbuser"
MARCOPASSWD = "lalaland"
DATABASE = "db_rentit"

def check_availability(category, table, column):
	"""Checks if category is already registered"""

	match = ""
	query = ("SELECT %s.* FROM %s WHERE %s.%s = '%s'" % (table,
														table,
														table,
														column,
														category))

	server = {"host" : MARCODB,
			"user" : MARCOUSER,
			"passwd" : MARCOPASSWD,
			"db" : DATABASE}
	db = DB(server)
	cursor = db.query(str(query))
	match = cursor.fetchall()

	if len(match) == 0:
		match = "False"
	else:
		match = "True"

	return match


def main():

	while 1:
		category = ""
		try:
			category = raw_input("Please enter product category: ")
		except EOFError as e:
			print "%s problem with category" % e

		if (check_availability(category, "products", "product_category") == "True"):
			print "Product \"%s\" found" % category
		else:
			print "No matches for category: %s. Would you like to create it?" % category



if __name__=="__main__":
	main()