import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import Photo
import Note
import Location
import Database
import Storage

database = Database.Database()
storage = Storage.Storage()


def login_( email, password ):
	response = database.login( email, password )
	return response

def create_account( last_name, first_name, email, password ):
	response = database.create_account( last_name, first_name, email, password )
	return response

def get_loc_photos( cur_user, cur_loc):
	response = database.get_loc_photos( cur_user, cur_loc )
	return response

def get_loc_notes( cur_user, cur_loc ):
	response = database.get_loc_notes( cur_user, cur_loc )
	return response

def get_all_locations( cur_user ):
	response = database.get_all_locations( cur_user )
	return response

def get_all_photos( cur_user ):
	response = database.get_all_photos( cur_user )
	return response

def get_all_notes( cur_user ):
	response = database.get_all_notes( cur_user )
	return response


server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."
server.register_function(login_, "login_")
server.register_function(create_account, "create_account")
server.register_function(get_loc_photos, "get_loc_photos")
server.register_function(get_loc_notes, "get_loc_notes")
server.register_function(get_all_locations, "get_all_locations")
server.register_function(get_all_photos, "get_all_photos")
server.register_function(get_all_notes, "get_all_notes")
server.serve_forever()












