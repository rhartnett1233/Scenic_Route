import Client
import Note
import Photo
import User
import Location


####################################
# Client Functions to Make
# login( username, password )
# create_account( last, first, email, password )
# get_all_locations( cur_user )
# get_all_photos( cur_user )
# get_all_notes( cur_user )


def first_screen( client ):
	print "Welcome to Scenic Route!"
	print "Enter the number for the following options:"
	print "1 \t --> Login"
	print "2 \t --> Create Account"
	print "3 \t --> Close Application"
	response = raw_input("")
	return response

def login( client ):
	valid_user = False
	email = raw_input( "Enter your email:  " )
	password = raw_input( "Enter your password:  " )
	user = cur_user.login( email, password )	#returns a user object
	return user

def create_account( client ):
	last_name = raw_input( "Enter your last name:  " )
	first_name = raw_input( "Enter your first name:  " )
	email = raw_input( "Enter your email address:  " )
	password = raw_input( "Enter your password:  " )
	user = client.create_account( last_name, first_name, email, password )	#returns a user object
	return user

def main_menu():
	print "MAIN MENU:"
	print "---------------------"
	print "Enter the number for the following options:"
	print "1\t\t-->\t\tView Locations"
	print "2\t\t-->\t\tView Photos"
	print "3\t\t-->\t\tView Notes"
	print "4\t\t-->\t\tEdit Account"
	print "5\t\t-->\t\tLogout"
	response = raw_input( "" )
	return response


##################################################################################
def display_location_photos( client, cur_user, cur_loc ):
	photo_list = client.get_loc_photos( cur_user, cur_loc )
	index = 1
	for photo in photo_list:
		print str(index) + "\t\t-->\t\t" + photo.file_name()
		index = index + 1
	raw_input( "ENTER TO RETURN" )

def display_location_notes( client, cur_user, cur_loc ):
	note_list = client.get_loc_notes( cur_user, cur_loc )
	index = 1
	for note in note_list:
		print "NOTE 1"
		print "---------------------"
		print note.get_text()
		print " "
	raw_input( "ENTER TO RETURN" )

def location( client, cur_user, cur_loc ):
	close_location = False
	while( close_location == False ):
		print cur_loc.get_name()
		print "---------------------"
		print "Enter the number for the following options:"
		print "0\t\t-->\t\tBACK TO LOCATIONS LIST"
		print "1\t\t-->\t\tView Photos"
		print "2\t\t-->\t\tView Notes"
		response = raw_input( "" )
		if( response == "0" ):
			close_location = True
		elif( response == "1" ):
			display_photos( client, cur_user, cur_loc )
		elif( response == "2" ):
			display_notes( client, cur_user, cur_loc )

def view_locations( client, cur_user ):
	close_locations_list = False
	while( close_location == False ):
		print "PICK A LOCATION:"
		print "---------------------"
		loc_list = client.get_all_locations( cur_user )
		index = 1
		print "0\t\t-->\t\tGO BACK TO MAIN MENU"
		for loc in loc_list:
			print str(index) + "\t\t-->\t\t" + loc.get_name()
			index = index + 1
		response = int( raw_input("") )
		if( response == 0 ):
			close_locations_list = True
		else:
			selected_loc = loc_list[ response-1 ]
			location( client, cur_user,selected_loc )
##################################################################################


close_application = False
while( close_application == False ):
	client = Client.Client()
	valid_user = False
	cur_user = None

	response = first_screen( client )
	# login
	if( response == "1" ):
		cur_user = login( client )
	#create account
	elif( response == "2" ):
		cur_user = create_account( client )
	#close application
	elif( response == "3" ):
		close_application = True

	if( cur_user != None ):
		logout_application = False
		while( logout_application == False ):
			response = main_menu()
			if( response == "1" ):
				loc_res = view_locations( client, cur_user )
			elif( response == "2" ):
				photo_res = view_photos( client, cur_user )
			elif( response == "3" ):
				note_res = view_notes( client, cur_user )
			elif( response == "4" ):
				edit_res = edit_account( client, cur_user )
			elif( response == "5" ):
				logout_application = True


	











