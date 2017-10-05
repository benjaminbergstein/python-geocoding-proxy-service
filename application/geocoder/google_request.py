import urllib.request
import urllib.parse
import json

class GoogleRequest:
	def __init__(self, address):
		self.address = address

	def geocode(self):
		params = {
			"address": self.address
		}

		endpoint = 'https://maps.googleapis.com/maps/api/geocode/json'
		url = '{0}?{1}'.format(endpoint, urllib.parse.urlencode(params))
		request_handler = urllib.request.urlopen(url)
		response_code = request_handler.getcode()
		response_body = request_handler.read().decode('utf-8')
		json_data = json.loads(response_body)
		return json_data['results'][0]['geometry']['location']
