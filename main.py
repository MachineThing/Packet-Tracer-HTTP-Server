from http import *
from time import *
from guiman import log

def onRouteRoot(url, resp):
	log(1, "Request for /");
	resp.setContentType("text/html")
	resp.sendFile("/index.html")
	
def onRouteCss(url, resp):
	log(1, "Request for /style.css")
	resp.setContentType("text/css")
	resp.sendFile("/style.css")

def onRouteWildcard(url, resp):
	log(1, "Request for " + url)
	resp.setContentType("text/html")
	resp.send("404")

def main():
	HTTPServer.route("/", onRouteRoot)
	HTTPServer.route("/style.css", onRouteCss)
	HTTPServer.route("/*", onRouteWildcard)

	# start server on port 80
	if HTTPServer.start(80) == True:
		log(1, "HTTP Server started!")
	else:
		log(3, "HTTP Server failed to start!")

	# don't let it finish
	while True:
		sleep(3600)

if __name__ == "__main__":
	main()
