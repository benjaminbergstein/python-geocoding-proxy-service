from BaseHTTPServer import BaseHTTPRequestHandler
from urlparse import urlparse, parse_qs
import json

class Application(BaseHTTPRequestHandler):
	def do_GET(self):
		uri = urlparse(self.path)
		query = parse_qs(uri.query)
		self.send_response(200)
		self.end_headers()
		self.wfile.write(json.dumps(query))
		return
