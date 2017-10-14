import MySQLdb

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
