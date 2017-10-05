from application.geocoder.base_request import BaseRequest

class HereRequest(BaseRequest):
	HOST = 'https://geocoder.cit.api.here.com'
	PATH = '/6.2/geocode.json'

	def params(self):
		return {
			"searchtext": self.address,
			"app_id": self.config.data['here_app_id'],
			"app_code": self.config.data['here_app_code']
		}

	def extract_coordinates_from_response(self, response):
		json_data = response.json()
		coordinates = json_data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']

		return {
			'lat': coordinates['Latitude'],
			'lng': coordinates['Longitude']
		}

