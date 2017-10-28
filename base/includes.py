import MySQLdb

MARCODB = "192.168.167.116"
MARCOUSER = "dbuser"
MARCOPASSWD = "lalaland"
DATABASE = "db_rentit"

class Table(object):
	"""A generic table object"""

	def __init__(self, *args, **kwargs):
		self.data = {}
		for dictionary in args:
			for key in dictionary:
				self.data.setdefault(key, dictionary[key])
		for key in kwargs:
			self.data.setdefault(key, kwargs[key])

class Creator(object):
	"""A helper for creating entries in db_rentit"""

	def __init__(self):
		self.name = "Creator"

	def createProduct(self, table):
		"""Received a Table object and builds a query based on key:value"""


		keys = table.data.keys()
		query = "INSERT INTO products ("
		for idx,k in enumerate(keys):
			if idx != len(keys) - 1:
				query += "%s, " % k
			else:
				query += "%s) " % k

		query += "VALUES ("
		for idx,k in enumerate(keys):
			if idx != len(keys) - 1:
				query += "\'%s\', " % table.data[k]
			else:
				query += "\'%s\');" % table.data[k]

		server = {"host" : MARCODB,
				"user" : MARCOUSER,
				"passwd" : MARCOPASSWD,
				"db" : DATABASE}

		db = DB(server)
		db.singleQuery(str(query))


class Checker(object):
	"""A helper for reading db_rentit"""

	def __init__(self):
		self.name = "Checker"

	@staticmethod
	def check_availability(value, table, column):
		"""Checks if value is already registered"""

		match = ""
		query = ("SELECT %s.* FROM %s WHERE %s.%s = '%s'" % (table,
															table,
															table,
															column,
															value))

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

class DB(object):
	def __init__(self, *args, **kwargs):
		for dictionary in args:
			for key in dictionary:
				setattr(self, key, dictionary[key])
		for key in kwargs:
			setattr(self, key, kwargs[key])

		self.conn = None
		self.connect()

	def connect(self):
		"""Establishes the connection to remode MySQL server"""

		self.conn = MySQLdb.connect(host=str(self.host),
									user=str(self.user),
									passwd=str(self.passwd),
									db=str(self.db))

	def singleQuery(self, sql):
		"""Does a query but does not return the cursor"""

		try:
			cursor = self.conn.cursor()
			cursor.execute(sql)
		except (AttributeError, MySQLdb.OperationalError):
			self.connect()
			cursor.execute(sql)
		finally:
			self.conn.commit()
			self.conn.close()



	def query(self, sql):
		"""Connects and sends a query to self.host"""

		try:
			cursor = self.conn.cursor()
			cursor.execute(sql)
		except (AttributeError, MySQLdb.OperationalError):
			self.connect()
			cursor.execute(sql)
		finally:
			self.conn.commit()
			return cursor
