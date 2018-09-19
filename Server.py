import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import Photo
import Note
import User
import Location
import Database
import Storage


def login_( email, password ):
	cur_user = database.login( email, password )
	return cur_user

def create_account( last_name, first_name, email, password ):
	cur_user = database.create_account( last_name, first_name, email, password )
	return cur_user

def get_loc_photos( cur_user, cur_loc):
	photo_list = storage.get_loc_photos( cur_user, cur_loc )
	return photo_list

def get_loc_notes( cur_user, cur_loc ):
	note_list = storage.get_loc_notes( cur_user, cur_loc )
	return note_list

def get_all_locations( cur_user ):
	loc_list = storage.get_all_locations( cur_user )
	return loc_list

def get_all_photos( cur_user ):
	photo_list = storage.get_all_photos( cur_user )
	return photo_list

def get_all_notes( cur_user ):
	note_list = storage.get_all_notes( cur_user )
	return note_list


server = SimpleXMLRPCServer(("localhost", 8000))
database = Database.Database()
storage = Storage.Storage()
print "Listening on port 8000..."
server.register_function(login_, "login_")
server.register_function(create_account, "create_account")
server.register_function(get_loc_photos, "get_loc_photos")
server.register_function(get_loc_notes, "get_loc_notes")
server.register_function(get_all_locations, "get_all_locations")
server.register_function(get_all_photos, "get_all_photos")
server.register_function(get_all_notes, "get_all_notes")
server.serve_forever()












