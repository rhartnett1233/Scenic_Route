


class Note:

	def __init__( self, date, location, text ):
		self.date = date
		self.location = location
		self.text = text

	def get_date( self ):
		return self.date

	def set_date( self, date ):
		self.date = date

	def get_location( self ):
		return self.location

	def set_location( self, location ):
		self.location = location

	def get_text( self ):
		return self.text

	def set_text( self, text ):
		self.text = text

	