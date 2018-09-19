import User
import Note
import Photo
import Location
import xmlrpclib

SERVER_ADDR = "http://localhost:8000/"

class Client:

	def __init__( self ):
		self.server = xmlrpclib.ServerProxy(SERVER_ADDR)


	def login( self, email, password ):
		cur_user = self.server.login_( email, password )
		return cur_user

	def create_account( self, last_name, first_name, email, password ):
		cur_user = self.server.create_account( last_name, first_name, email, password )
		return cur_user

	def get_loc_photos( self, cur_user, cur_loc ):
		photo_list = self.server.get_loc_photos( cur_user, cur_loc )
		return photo_list

	def get_loc_notes( self, cur_user, cur_loc ):
		note_list = self.server.get_loc_notes( cur_user, cur_loc )
		return note_list

	def get_all_locations( self, cur_user ):
		loc_list = self.server.get_all_locations( cur_user )
		return loc_list

	def get_all_photos( self, cur_user ):
		photo_list = self.server.get_all_photos( cur_user )
		return photo_list

	def get_all_notes( self, cur_user ):
		note_list = self.server.get_all_notes( cur_user )
		return note_list











