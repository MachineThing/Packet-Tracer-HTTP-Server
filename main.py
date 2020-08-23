from http import *
from time import *
from guiman import log

class http_page:
	def __init__(self, file, mimetype="text/html"):
		self.file = file
		self.mimetype = mimetype
	def get_page(self, path, resp):
		log(1, "Request for \""+path+"\"")
		resp.setContentType(self.mimetype)
		print(self.file, path)
		resp.sendFile(self.file)
	def route(self, path):
		HTTPServer.route(path, self.get_page)

# HTML Files
index = http_page("/index.html")
page_not_found = http_page("/404.html")

# CSS Files

styles = http_page("/style.css", "text/css")

def main():
	index.route("/")
	page_not_found.route("/*")
	styles.route("/style.css")

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
