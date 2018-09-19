import User
import Location
import Note
import Photo


class Database:


	def __init__( self ):
		temp = True

	def login( self, email, password ):
		response = [ "Hartnett", "Richie", email, password ]
		cur_user = User.User( str(response[0]), str(response[1]), str(response[2]), str(response[3]) )
		return cur_user

	def create_account( self, last_name, first_name, email, password ):
		cur_user = User.User( last_name, first_name, email, password )
		return cur_user
