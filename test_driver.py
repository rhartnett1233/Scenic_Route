import Client
import Note
import Photo
import Location




client = Client.Client()
photo_list = []
note_list = []
cur_loc = Location.Location( "Westport", 41.512069, -71.069369, photo_list, note_list )

cur_user = client.login( "rhartnett", "strider" )
client.create_account( "hartnett", "richie", "rhartnett", "strider" )
client.get_loc_photos( cur_user, cur_loc )
client.get_loc_notes( cur_user, cur_loc )
client.get_loc_notes( cur_user, cur_loc )
client.get_all_locations( cur_user )
client.get_all_photos( cur_user )
client.get_all_notes( cur_user )
