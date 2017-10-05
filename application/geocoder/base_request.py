import logging

class BaseRequest:
	def __init__(self, config, address, http_connection):
		self.config = config
		self.address = address
		self.http_connection = http_connection

	def geocode(self):
		response = self.perform_request()

		if response is False:
			return False

		coordinates = self.extract_coordinates_from_response(response)

		return coordinates

	def perform_request(self):
		response = self.http_connection.get_url(self.HOST, self.PATH, self.params())

		if response.code is 200:
			return response
		else:
			return False
