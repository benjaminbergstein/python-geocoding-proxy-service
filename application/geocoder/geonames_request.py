from application.geocoder.base_request import BaseRequest
import logging

class GeonamesRequest(BaseRequest):
	HOST = 'http://api.geonames.org'
	PATH = '/geocode'

	def params(self):
		return {
			'q': self.address,
			'username': self.config.data['geonames_username']
		}

	def extract_coordinates_from_response(self, response):
		xml = response.xml()
		coordinates_xml = xml.find('geoCoderResult')

		return {
			'lat': coordinates_xml.find('lat').text,
			'lng': coordinates_xml.find('lng').text
		}
