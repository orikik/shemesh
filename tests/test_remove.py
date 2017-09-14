import unittest
import requests
import mongo


class MyTestCase(unittest.TestCase):
    params = {
        'username': 'testing',
        'password': '1234'
    }

    api_url = mongo.api_url + 'remove'

    def test_remove_post(self):
        requests.post(url=mongo.api_url + 'registration', json=self.params)
        requests.post(url=mongo.api_url + 'login', json=self.params)
        requests.post(url=self.api_url, json=self.params)
        self.assertFalse(mongo.collection.find_one({"username": self.params['username']}))

    def test_remove_get(self):
        requests.post(url=mongo.api_url + 'registration', json=self.params)
        session = requests.Session()
        response = session.get(url=mongo.api_url + "login")
        c = response.cookies
        requests.get(url=mongo.api_url + "remove", cookies=c)
        self.assertFalse(mongo.collection.find_one({"username": self.params['username']}))
        requests.post(url=mongo.api_url + 'remove', json=self.params)

    def test_remove_all(self):
        params = {
            'username': 'testing',
            'password': '1234'
        }
        params_dir0 = {
            'name': 'name0'
        }
        params_file0 = {
            'my_path': 'C:/фотки/9.txt',
            'storage_path': 'name0'
        }
        params_file1 = {
            'my_path': 'C:/фотки/11.txt',
        }
        requests.post(url=mongo.api_url + 'registration', json=params)
        session = requests.Session()
        response = session.post(url=mongo.api_url + "login", json=params)
        c = response.cookies
        requests.post(url=mongo.api_url + 'new_dir', cookies=c, json=params_dir0)
        requests.post(url=mongo.api_url + 'upload', cookies=c, json=params_file0)
        requests.post(url=mongo.api_url + 'upload', cookies=c, json=params_file1)
        username = mongo.collection.find_one({'username': params['username']})
        id = str(username['_id'])
        requests.post(url=mongo.api_url + 'remove', json=params)
        self.assertFalse(mongo.file_collection.find_one({'username': id}))
        self.assertFalse(mongo.dir_collection.find_one({'username': id}))

if __name__ == '__main__':
    unittest.main()
