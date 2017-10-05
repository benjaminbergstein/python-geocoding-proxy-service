import urllib.request
import urllib.parse
import unittest, os, sys, json

from application.geocoder import Geocoder

sightglass_coordinates = {
  'lat': 37.7769813,
  'lng': -122.4085708
}

class ServerTestCase(unittest.TestCase):
  def fetch_endpoint(self, path):
    url = 'http://localhost:8000{0}'.format(path)
    request_handler = urllib.request.urlopen(url)
    response_body = request_handler.read().decode('utf-8')
    return json.loads(response_body)

  def test_basic_request(self):
    response = self.fetch_endpoint('/?address=270%207th%20St,%20San%20Francisco,%20CA%2094103')
    self.assertEqual(sightglass_coordinates, response)

class GeocoderTest(unittest.TestCase):
  def test_basic(self):
    address = '270 7th St, San Francisco, CA 94103'
    geocoder = Geocoder()
    geocoder_response = geocoder.geocode(address)
    self.assertEqual(sightglass_coordinates, geocoder_response)

if __name__ == '__main__':
    unittest.main()
