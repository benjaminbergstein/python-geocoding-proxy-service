from application.geocoder.base_request import BaseRequest

class GoogleRequest(BaseRequest):
	HOST = 'https://maps.googleapis.com'
	PATH = '/maps/api/geocode/json'

	def params(self):
		return {
			"address": self.address
		}

	def extract_coordinates_from_response(self, response):
		data = response.json()
		return data['results'][0]['geometry']['location']
