import urllib.request
import urllib.parse
import json
from application.http_connection.response import Response

class HttpConnection:
	def get_url(self, host, path, parameters):
		full_url = '{0}{1}?{2}'.format(host, path, self.encode_parameters(parameters))

		try:
			request_handler = self.perform_get(full_url)
		except urllib.request.URLError as e:
			return Response(None, e)
		else:
			return Response(request_handler, None)

	def perform_get(self, url):
		return urllib.request.urlopen(url)

	def encode_parameters(self, parameters):
		return urllib.parse.urlencode(parameters)
