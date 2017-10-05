import urllib.request
import urllib.parse
import json
from application.http_connection.response import Response

class HttpConnection:
  def get_url(self, host, path, parameters):
    full_url = '{0}{1}?{2}'.format(host, path, self.encode_parameters(parameters))
    request_handler = urllib.request.urlopen(full_url)
    return Response(request_handler)

  def encode_parameters(self, parameters):
    return urllib.parse.urlencode(parameters)
