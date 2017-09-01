import shutil

import os

import mongo

class dev():
    def __init__(self):
        pass

    def choose_device(self):
        space = 0
        for men in mongo.dev_collection.find():
            if men['free space'] > space:
                space = men['free space']
        dev = mongo.dev_collection.find_one({'free space':space})
        return dev['path']

    def copy(self, username, path_from, path_to = ''):
        dev_path = self.choose_device()
        size = os.path.getsize(path_from)
        if mongo.dev_collection.find_one({'path': dev_path})['free space']>=size:
            dir_path = self.path_exist(dev_path, username, path_to)
            shutil.copy2(path_from, dev_path + dir_path)
            mongo.dev_collection.update({'path': dev_path}, {'$inc': {'used space': size, 'free space': -size}})
            params_file = {
                'username': username,
                'device': dev_path,
                'path': dir_path,
                'size': size
            }
            mongo.file_collection.save(params_file)
            return 'A new file added.'
        else:
            return 'All devices are full.'

    def path_exist(self, dev_path, username, path_to = ''):
        m = dev_path
        n = "/" + username + '/' + path_to
        if os.path.exists(m + n):
            return n
        else:
            os.mkdir(path=m + n)
            return n

