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
        if os.path.isfile(path_from):
            dev_path = self.choose_device()
            size = os.path.getsize(path_from)
            if mongo.dev_collection.find_one({'path': dev_path})['free space']>=size:
                dir_path = self.path_exist(dev_path, username, path_to)
                name = os.path.basename(path_from)
                if not mongo.file_collection.find_one({'username': username, 'path': dir_path, 'name': name}):
                    shutil.copy2(path_from, dev_path + dir_path)
                    mongo.dev_collection.update({'path': dev_path}, {'$inc': {'used space': size, 'free space': -size}})
                    params_file = {
                        'username': username,
                        'device': dev_path,
                        'path': dir_path,
                        'size': size,
                        'name': name
                    }
                    mongo.file_collection.save(params_file)
                    return 'A new file added.'
                else:
                    return 'A file with this name already exists.'
            else:
                return 'All devices are full.'
        else:
            return 'Specify the full path.'

    def path_exist(self, dev_path, username, path_to = ''):
        m = dev_path
        n = "/" + username + '/' + path_to
        if os.path.exists(m + n):
            return n
        else:
            os.mkdir(path=m + n)
            return n

    def dir_exist(self):
        pass

    def user_path(self, data, username):
        key1 = 'path' in data
        key2 = 'directory' in data
        if key1 == True and key2 == True and len(data) == 2:
            n = self.copy(username=username, path_from=data['path'], path_to=data['directory'])
            return n
        elif key1 == True and len(data) == 1:
            n = self.copy(username=username, path_from=data['path'])
            return n

    def remove_file(self, username, name, path_from=''):
        path = '/' + username + '/' + path_from
        n = mongo.file_collection.find_one({'username': username, 'name': name, 'path': path})
        os.remove(n['device']+n['path']+n['name'])
        mongo.file_collection.remove(n)
        mongo.dev_collection.update({'path': n['device']}, {'$inc': {'used space': -n['size'], 'free space': n['size']}})
        return 'file delete'

