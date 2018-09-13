

class User:

	def __init__( self, last, first, email, password ):
		self.last_name = last
		self.first_name = first
		self.email = email
		self.password = password


	def get_last_name( self ):
		return self.last_name

	def set_last_name( self, last ):
		self.last_name = last

	def get_first_name( self ):
		return self.first_name

	def set_first_name( self, first ):
		self.first_name = first

	def get_email( self ):
		return self.email

	def set_email( self, username ):
		self.email = email

	def get_password( self ):
		return self.password

	def set_password( self, password ):
		self.password = password
