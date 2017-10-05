import json
import xml.etree.ElementTree as ET

class Response:
	def __init__(self, handler = None, error = None):
		if handler is None and error is None:
			raise BaseException('uhoh')

		if handler is not None:
			self.handler = handler
			self.code = handler.getcode()
			self.body = handler.read().decode('utf-8')

		if error is not None:
			self.error = error
			self.code = error.code
			self.body = error.reason

	def json(self):
		return json.loads(self.body)

	def xml(self):
		tree = ET.fromstring(self.body)
		return tree
