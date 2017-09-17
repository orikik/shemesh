import unittest
import mongo
import requests


class MyTestCase(unittest.TestCase):
    params = {
        'username': 'testing',
        'password': '1234'
    }
    params_dir0 = {
        'name': 'name0'
    }
    params_dir1 = {
        'path': 'name0',
        'name': 'name1'
    }
    params_file0 = {
        'my_path': 'C:/work/shemesh/tests/test.txt',
        'storage_path': 'name0'
    }
    params_file1 = {
        'my_path': 'C:/work/shemesh/tests/test.txt',
        'storage_path': 'name0/name1'
    }
    requests.post(url=mongo.api_url + 'registration', json=params)
    session = requests.Session()
    response = session.post(url=mongo.api_url + "login", json=params)
    c = response.cookies
    api_url = mongo.api_url + 'new_dir'

    def test_remove_dir(self):
        requests.post(url=self.api_url, cookies=self.c, json=self.params_dir0)
        requests.post(url=self.api_url, cookies=self.c, json=self.params_dir1)
        requests.post(url=mongo.api_url + 'upload', cookies=self.c, json=self.params_file0)
        requests.post(url=mongo.api_url + 'upload', cookies=self.c,json=self.params_file1)
        requests.post(url=mongo.api_url + 'remove_dir', cookies=self.c, json=self.params_dir0)
        username = mongo.collection.find_one({'username': self.params['username']})
        id = str(username['_id'])
        self.assertFalse(mongo.dir_collection.find_one({"name": self.params_dir0['name']}))
        self.assertFalse(mongo.dir_collection.find_one({"name": self.params_dir1['name'],
                                                       'path1': self.params_dir1['path']}))
        self.assertFalse(mongo.file_collection.find_one({'path': id + '/' + self.params_file0['storage_path']}))
        self.assertFalse(mongo.file_collection.find_one({'path': id + '/' + self.params_file1['storage_path']}))
        requests.post(url=mongo.api_url + 'remove', json=self.params)


if __name__ == '__main__':
    unittest.main()
