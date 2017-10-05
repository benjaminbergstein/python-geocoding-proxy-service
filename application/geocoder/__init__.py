from application.geocoder.google_request import GoogleRequest

class Geocoder:
  def geocode(self, address):
    google_request = GoogleRequest(address)
    return google_request.geocode()