CLASSPATH=./lib/commons-codec-1.3.jar:./lib/xmlrpc-2.0.1.jar:.

all: hello

hello: test_driver.pyc Client.pyc Server.pyc
	python test_driver.pyc Client.pyc Server.pyc

driver: test_driver.pyc Client.pyc runtestdriver

server: Server.pyc runserver

runtestdriver:
	@python -classpath $(CLASSPATH) test_driver

runserver:
	@python -classpath $(CLASSPATH) Server

test_driver.pyc: test_driver.py
	python test_driver.py

Client.pyc: Client.py
	python Client.py

Server.pyc: Server.py
	python Server.py

clean:
	rm *pyc hello