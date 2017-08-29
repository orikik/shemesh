import requests

import mongo


class Params:
    user = {
        'username': 'testing',
        'password': '1234'
    }

    def registr(self):
        api_url = mongo.api_url + 'register'
        requests.post(url=api_url, json=self.user)
