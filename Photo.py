

class Photo:

	def __init__( self, date, location, filename ):
		self.date = date
		self.location = location
		self.filename = filename

	def get_date( self ):
		return self.date

	def set_date( self, date ):
		self.date = date

	def get_location( self ):
		return self.location

	def set_location( self, location ):
		self.location = location

	def get_filename( self ):
		return self.filename

	def set_filename( self, filename ):
		self.filename = filename