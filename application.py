from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from geocoder import Geocoder

class Application(BaseHTTPRequestHandler):
	def __init__(self):
		self.config = self.load_config()
		self.geocoder = Geocoder(self)

	def load_config(self):
		config_file = open('./secrets.json', 'r')
		config_data = json.loads(config_file.read())
		config_file.close()
		return config_data
