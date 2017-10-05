import urllib.request
import urllib.parse
import unittest, os, sys, json
from unittest import mock

from application.config import Config
from application.geocoder import Geocoder
from application.geocoder.geonames_request import GeonamesRequest
from application.geocoder.here_request import HereRequest
from application.http_connection import HttpConnection
from application.http_connection.response import Response

sightglass_coordinates_from_google = {
	'lat': 37.7768998,
	'lng': -122.4086371
}

sightglass_coordinates_from_geonames = {
	'lat': '37.777098',
	'lng': '-122.408283'
}

sightglass_coordinates_from_here = {
	'lat': 37.77696,
	'lng': -122.40851
}

real_http_connection = HttpConnection()
config = Config()

class ServerTestCase(unittest.TestCase):
 	def fetch_endpoint(self, path):
 		url = 'http://localhost:8000{0}'.format(path)
 		request_handler = urllib.request.urlopen(url)
 		response_body = request_handler.read().decode('utf-8')
 		return json.loads(response_body)

 	def test_basic_request(self):
 		response = self.fetch_endpoint('/?address=270%207th%20St,%20San%20Francisco,%20CA%2094103')
 		self.assertEqual(sightglass_coordinates_from_google, response)

class GeocoderTest(unittest.TestCase):
	def test_basic(self):
		address = '270 7th St, San Francisco, CA 94103'
		geocoder = Geocoder(HttpConnection())
		geocoder_response = geocoder.geocode(address)
		self.assertEqual(sightglass_coordinates_from_google, geocoder_response)

	def fake_get_url(host, path, parameters):
		if host in self.problem_hosts:
			return response
		else:
			return real_http_connection.get_url(host, path, parameters)

	@mock.patch('__main__.HttpConnection')
	@mock.patch('__main__.Response')
	def test_google_isnt_working(self, http_connection, response):
		address = '270 7th St, San Francisco, CA 94103'
		response.code = 500

		fake_response_helper = FakeResponseHelper(
			['https://maps.googleapis.com'],
			response,
			real_http_connection
		)

		http_connection.get_url = fake_response_helper.get_url_method()
		geocoder = Geocoder(http_connection)
		geocoder_response = geocoder.geocode(address)
		self.assertEqual(sightglass_coordinates_from_geonames, geocoder_response)

	@mock.patch('__main__.HttpConnection')
	@mock.patch('__main__.Response')
	def test_google_and_geonames_arent_working(self, http_connection, response):
		address = '270 7th St, San Francisco, CA 94103'
		response.code = 500

		fake_response_helper = FakeResponseHelper(
			['https://maps.googleapis.com', 'http://api.geonames.org'],
			response,
			real_http_connection
		)

		http_connection.get_url = fake_response_helper.get_url_method()
		geocoder = Geocoder(http_connection)
		geocoder_response = geocoder.geocode(address)
		self.assertEqual(sightglass_coordinates_from_here, geocoder_response)

class GeonamesRequestTestCase(unittest.TestCase):
	def test_xml(self):
		address = '270 7th St, San Francisco, CA 94103'
		http_connection = HttpConnection()
		geonames_request = GeonamesRequest(config, address, http_connection)
		geocoder_response = geonames_request.geocode()
		self.assertEqual(sightglass_coordinates_from_geonames, geocoder_response)

class HereRequestTestCase(unittest.TestCase):
	def test_request(self):
		address = '270 7th St, San Francisco, CA 94103'
		http_connection = HttpConnection()
		here_request = HereRequest(config, address, http_connection)
		geocoder_response = here_request.geocode()
		self.assertEqual(sightglass_coordinates_from_here, geocoder_response)

class ConfigTestCase(unittest.TestCase):
	def test_load_config(self):
		config = Config()
		self.assertEqual(list(config.data.keys()), [ 'geonames_username', 'here_app_id', 'here_app_code' ])

class FakeResponseHelper:
	def __init__(self, problem_hosts, fake_response, real_http_connection):
		self.problem_hosts = problem_hosts
		self.fake_response = fake_response
		self.real_http_connection = real_http_connection

	def get_url_method(self):
		def get_url(host, path, parameters):
			if host in self.problem_hosts:
				return self.fake_response
			else:
				return self.real_http_connection.get_url(host, path, parameters)
		return get_url

if __name__ == '__main__':
		unittest.main()
