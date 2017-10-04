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
    response = self.fetch_endpoint('/?address=270%207th%20St,%20San%20Francisco,%20CA%2094103')
    self.assertEqual({ 'address': ['270 7th St, San Francisco, CA 94103'] }, response)

if __name__ == '__main__':
    unittest.main()
