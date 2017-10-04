import urllib.request
import urllib.parse
import unittest
import json

class ServerTestCase(unittest.TestCase):
  def fetch_endpoint(self, path):
    url = 'http://localhost:8000{0}'.format(path)
    request_handler = urllib.request.urlopen(url)
    return json.loads(request_handler.read().decode('utf-8'))

  def test_basic_request(self):
    self.assertEqual(self.fetch_endpoint('/'), {'data': 'banana'})

if __name__ == '__main__':
    unittest.main()
