import json
import xml.etree.ElementTree as ET

class Response:
	def __init__(self, handler):
		self.handler = handler
		self.code = handler.getcode()
		self.body = handler.read().decode('utf-8')

	def json(self):
		return json.loads(self.body)

	def xml(self):
		tree = ET.fromstring(self.body)
		return tree
