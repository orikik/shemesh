import mongo


class DB_dir:
    def dir_exists(self, username, full_path):
        if mongo.dir_collection.find_one({'username': username, 'full path': full_path}):
            return True
        else:
            return False

    def dir_exist(self, username, name, full_path):
        n = mongo.dir_collection.find_one({'username': username, 'name': name, 'full path': full_path})
        if n:
            return n
        else:
            return False

    def path_to_dir_exist(self, username, dir_path):
        if mongo.dir_collection.find_one({'username': username, 'full path': dir_path}):
            return True
        else:
            return False

    def add_dir(self, username, name, full_path):
        params = {
            'username': username,
            'name': name,
            'full path': full_path
        }
        mongo.dir_collection.save(params)
        return 'A new directory created.'

    def remove_dir(self, data):
        mongo.dir_collection.remove(data)
        return 'The directory was deleted.'

    def dir_update(self, new_name, data):
        mongo.dir_collection.update(data, {'name': new_name})
        return 'The directory name has been changed.'

    def find_files_in_dir(self, username, path, d):
        for files in mongo.file_collection.find({'username': username, 'path': path}):
            d.append(files['name'])
        return d