import json
from application.http_connection import HttpConnection
from application.geocoder import Geocoder

def handler(event, context):
	address = extract_address(event)

	if address is None:
		return send_json(400, {
			'message': 'Please provide an address to geocode your request query string (e.g. "?address=Google%20Headquarters")'
		})

	coordinates = perform_geocoding(address)

	if coordinates is False:
		return 	send_json(503, {
			'message': 'There are no geocoding services available. Try again later.'
		})
	else:
		return send_json(200, coordinates)

def extract_address(event):
	params = event.get('queryStringParameters')

	if params is not None:
		return params.get('address')

def send_json(code, body):
	return {
			"isBase64Encoded": False,
			"statusCode": code,
			"headers": {},
			"body": json.dumps(body)
	}

def perform_geocoding(address):
	http_connection = HttpConnection()
	geocoder = Geocoder(http_connection)
	coordinates = geocoder.geocode(address)
	return coordinates
