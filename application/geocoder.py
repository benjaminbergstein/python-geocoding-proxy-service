import urllib.request
import urllib.parse
import json

class Geocoder:
  def __init__(self, application):
    self.application = application

  def geocode(self, address):
    response = self.fetch_response(address)
    coordinates = response['results'][0]['geometry']['location']
    return coordinates

  def fetch_response(self, address):
    params = {
      address: address
    }

    google_config = self.application.config['google']
    if google_config and google_config['api_key']:
      params['key'] = google_config['api_key']

    endpoint = 'https://maps.googleapis.com/maps/api/geocode/json'
    url = '{0}?address={1}'.format(endpoint, urllib.parse.urlencode(params))
    request_handler = urllib.request.urlopen(url)
    response_body = request_handler.read().decode('utf-8')
    return json.loads(response_body)
