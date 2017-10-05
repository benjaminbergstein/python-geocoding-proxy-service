import json

class Config:
	def __init__(self):
		secrets_file = open('./secrets.json')
		self.data = json.loads(secrets_file.read())
		secrets_file.close()