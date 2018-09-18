import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

def login_( email, password ):
	response = [ "Hartnett", "Richie", email, password ]
	print email
	print password
	return response

def createAccount( last_name, first_name, email, password ):
	return 1

server = SimpleXMLRPCServer(("localhost", 8000))
print "Listening on port 8000..."
server.register_function(login_, "login_")
server.serve_forever()