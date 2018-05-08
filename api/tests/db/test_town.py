import os

print(os.getcwd())
from api.tests import test_api
import requests, json


class TownTest(test_api.APITest):
	def test_add(self):
		town_to_add = {'name':'Town One', 'region':'Region One'}
		r = requests.post('http://localhost:8090/interact/add_town', json=town_to_add)
		assert (r.status_code == 200)
		return