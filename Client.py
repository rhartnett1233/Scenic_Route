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
		response = self.server.login_( email, password )
		return response

	def create_account( self, last_name, first_name, email, password ):
		response = self.server.create_account( last_name, first_name, email, password )
		if( int(response) == 1 ):
			cur_user = User.User( last_name, first_name, email, password )
		else:
			cur_user = None
		return cur_user

	def get_loc_photos( self, cur_user, cur_loc ):
		response = self.server.get_loc_photos( cur_user, cur_loc )
		return response

	def get_loc_notes( self, cur_user, cur_loc ):
		response = self.server.get_loc_notes( cur_user, cur_loc )
		return response

	def get_all_locations( self, cur_user ):
		response = self.server.get_all_locations( cur_user )
		return response

	def get_all_photos( self, cur_user ):
		response = self.server.get_all_photos( cur_user )
		return response

	def get_all_notes( self, cur_user ):
		response = self.server.get_all_notes( cur_user )
		return response











