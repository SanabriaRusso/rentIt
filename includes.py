import MySQLdb

MARCODB = "192.168.167.116"
MARCOUSER = "dbuser"
MARCOPASSWD = "lalaland"
DATABASE = "db_rentit"

class Checker(object):
	"""A helper for reading db_rentit"""

	def __init__(self):
		self.name = "Checker"

	@staticmethod
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
