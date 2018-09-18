import Client
import Note
import Photo
import Location




client = Client.Client()

cur_user = client.login( "rhartnett", "strider" )
print cur_user.get_last_name()