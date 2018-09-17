import User
import Note
import Photo
import Location


class Client:


	def __init__( self ):
		photo1 = Photo.Photo( "03/11/1996", "Westport", "img1.jpg" )
		photo2 = Photo.Photo( "04/11/1996", "Westport", "img2.jpg" )
		photo3 = Photo.Photo( "03/19/1996", "Westport", "img3.jpg" )
		photo4 = Photo.Photo( "06/18/2006", "Westport", "img4.jpg" )
		photo5 = Photo.Photo( "10/31/1992", "Westport", "img5.jpg" )
		photo6 = Photo.Photo( "01/13/1990", "Westport", "img6.jpg" )
		self.photo_list = [ photo1, photo2, photo3, photo4, photo5, photo6 ]
		note1 = Note.Note( "09/13/2018", "Westport", "THis is my first note on Scenic Route. I am probably going to quit this very soon." )
		note2 = Note.Note( "09/13/2018", "Westport", "THis is my second note on Scenic Route. I am very stoned right now" )
		self.note_list = [ note1, note2 ]
		
		self.cur_loc = Location.Location( "Westport", 41.512069, -71.069369, self.photo_list, self.note_list )


	def login( self, email, password ):
		cur_user = User.User( "Hartnett", "Richie", "email", "strider" )
		return cur_user

	def create_account( self, last_name, first_name, email, password ):
		cur_user = User.User( last_name, first_name, email, password )
		return cur_user

	def get_loc_photos( self, cur_user, cur_loc ):
		return self.photo_list

	def get_loc_notes( self, cur_user, cur_loc ):
		return self.note_list

	def get_all_locations( self, cur_user ):
		loc1 = Location.Location( "Westport", 41.512069, -71.069369, self.photo_list, self.note_list )
		loc2 = Location.Location( "California", 12.512069, -110.069369, self.photo_list, self.note_list )
		loc3 = Location.Location( "Tampa", 100.512069, -3.069369, self.photo_list, self.note_list )
		loc_list = [ loc1, loc2, loc3 ]
		return loc_list

	def get_all_photos( self, cur_user ):
		return self.photo_list

	def get_all_notes( self, cur_user ):
		return self. note_list











