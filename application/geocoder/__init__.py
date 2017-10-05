from application.config import Config
from application.geocoder.google_request import GoogleRequest
from application.geocoder.here_request import HereRequest
from application.geocoder.geonames_request import GeonamesRequest

class Geocoder:
	def __init__(self, http_connection):
		self.config = Config()
		self.http_connection = http_connection

	def geocode(self, address):
		google_request = GoogleRequest(self.config, address, self.http_connection)
		here_request = HereRequest(self.config, address, self.http_connection)
		geonames_request = GeonamesRequest(self.config, address, self.http_connection)

		result = google_request.geocode()

		if result == False:
			result = geonames_request.geocode()

		if result == False:
			result = here_request.geocode()

		return result
