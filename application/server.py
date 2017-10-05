from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from application import Application

class Server(BaseHTTPRequestHandler):
	def do_GET(self):
		coordinates = self.perform_geocoding()
		self.send_json(200, coordinates)
		return

	def perform_geocoding(self):
		application = Application()
		uri = urlparse(self.path)
		query = parse_qs(uri.query)
		coordinates = application.geocoder.geocode(query['address'][0])
		return coordinates

	def send_json(self, http_status_code, data):
		response_text = json.dumps(data)
		self.send_response(http_status_code)
		self.end_headers()
		self.wfile.write(response_text.encode('utf-8'))
		return