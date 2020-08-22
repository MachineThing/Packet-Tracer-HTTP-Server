from http import *
from time import *
from guiman import log

def onRouteRoot(url, response):
	log(1, "Request for /");
	response.send("Goodbye cruel world!")
	
def onRouteTest(url, response):
	log(1, "Request for /test")
	response.send("test content")
	
def onRouteFile(url, response):
	log(1, "Request for /file")
	response.sendFile("/file.txt")

def onRouteWildcard(url, response):
	log(1, "Request for " + url)
	response.send("404")

def main():
	HTTPServer.route("/", onRouteRoot)
	#HTTPServer.route("/test", onRouteTest)
	#HTTPServer.route("/file", onRouteFile)
	HTTPServer.route("/*", onRouteWildcard)

	# start server on port 80
	log(1, HTTPServer.start(80))

	# don't let it finish
	while True:
		sleep(3600)

if __name__ == "__main__":
	main()
