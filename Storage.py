import User
import Location
import Photo
import Note


class Storage:


	def __init__( self ):
		temp = True


	def get_loc_photos( self, cur_user, cur_loc):
		photo1 = Photo.Photo( "03/11/1996", "Westport", "img1.jpg" )
		photo2 = Photo.Photo( "04/11/1996", "Westport", "img2.jpg" )
		photo3 = Photo.Photo( "03/19/1996", "Westport", "img3.jpg" )
		photo4 = Photo.Photo( "06/18/2006", "Westport", "img4.jpg" )
		photo5 = Photo.Photo( "10/31/1992", "Westport", "img5.jpg" )
		photo6 = Photo.Photo( "01/13/1990", "Westport", "img6.jpg" )
		photo_list = [ photo1, photo2, photo3, photo4, photo5, photo6 ]
		return photo_list

	def get_loc_notes( self, cur_user, cur_loc ):
		note1 = Note.Note( "09/13/2018", "Westport", "THis is my first note on Scenic Route. I am probably going to quit this very soon." )
		note2 = Note.Note( "09/13/2018", "Westport", "THis is my second note on Scenic Route. I am very stoned right now" )
		note_list = [ note1, note2 ]
		return note_list

	def get_all_locations( self, cur_user ):
		photo_list = []
		note_list = []
		loc1 = Location.Location( "Westport", 41.512069, -71.069369, photo_list, note_list )
		loc2 = Location.Location( "California", 12.512069, -110.069369, photo_list, note_list )
		loc3 = Location.Location( "Tampa", 100.512069, -3.069369, photo_list, note_list )
		loc_list = [ loc1, loc2, loc3 ]
		return loc_list

	def get_all_photos( self, cur_user ):
		photo1 = Photo.Photo( "03/11/1996", "Westport", "img1.jpg" )
		photo2 = Photo.Photo( "04/11/1996", "Westport", "img2.jpg" )
		photo3 = Photo.Photo( "03/19/1996", "Westport", "img3.jpg" )
		photo4 = Photo.Photo( "06/18/2006", "Westport", "img4.jpg" )
		photo5 = Photo.Photo( "10/31/1992", "Westport", "img5.jpg" )
		photo6 = Photo.Photo( "01/13/1990", "Westport", "img6.jpg" )
		photo_list = [ photo1, photo2, photo3, photo4, photo5, photo6 ]
		return photo_list

	def get_all_notes( self, cur_user ):
		note1 = Note.Note( "09/13/2018", "Westport", "THis is my first note on Scenic Route. I am probably going to quit this very soon." )
		note2 = Note.Note( "09/13/2018", "Westport", "THis is my second note on Scenic Route. I am very stoned right now" )
		note_list = [ note1, note2 ]
		return note_list