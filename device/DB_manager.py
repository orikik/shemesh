import mongo


class DB:
    def dir_exists(self, username, full_path):
        if mongo.dir_collection.find_one({'username': username, 'full path': full_path}):
            return True
        else:
            return False

    def file_exist(self, username, dir_path, name):
        if mongo.file_collection.find_one({'username': username, 'path': dir_path, 'name': name}):
            return True
        else:
            return False

    def all_dev(self):
        return mongo.dev_collection.find()

    def get_file(self, username, dir_path, name):
        if self.file_exist(username, dir_path, name):
            n = mongo.file_collection.find_one({'username': username, 'path': dir_path, 'name': name})
            return n
        else:
            return False

    def remove_file(self, file):
        size = file['size']
        dev_path = file['device']
        mongo.file_collection.remove(file)
        mongo.dev_collection.update({'path': dev_path}, {'$inc': {'used space': -size, 'free space': size}})

    def dev_size_find(self, dev_path):
        m = mongo.dev_collection.find_one({'path': dev_path})
        n = m['free space']
        return n

    def update_device(self, dev_path, size):
        mongo.dev_collection.update({'path': dev_path}, {'$inc': {'used space': size, 'free space': -size}})

    def update_files(self, params_file):
        mongo.file_collection.save(params_file)

    def get_device(self, space):
        n = mongo.dev_collection.find_one({'free space': space})
        return n