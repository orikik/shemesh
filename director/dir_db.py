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
        m = full_path.split('/')
        x = str(1)
        for n in m[1:-1]:
            mongo.dir_collection.update({'username': username, "full path":full_path}, {"$set": {"path"+x: n}})
            x = str(int(x) + 1)
        return 'A new directory created.'

    def remove_dir(self, data):
        mongo.dir_collection.remove(data)
        return 'The directory was deleted.'

    def dir_update(self, new_name, full_path):
        n = mongo.dir_collection.find_one({'full path':full_path})
        m = str(len(full_path.split('/'))-1)
        for path in mongo.dir_collection.find({'path' + m: n['name']}):
            b = DB_dir().dir_get_new_full_path(data=path, count=m, name=new_name)
            mongo.dir_collection.update(path, {"$set": {"path"+m: new_name}})
            mongo.dir_collection.update(path, {"$set": {"full path": b}})
        mongo.dir_collection.update(n, {"$set": {'name': new_name}})
        return 'The directory name has been changed.'

    def dir_get_new_full_path(self, data, count, name):
        m = len(data['full path'].split('/')) - 1
        path_to = ''
        for n in range(1, m):
            if n == count:
                path_to = path_to + name + '/'
            else:
                path_to = path_to + data['path'+str(n)] + '/'
        full_path = data['username'] + '/' + path_to + data['name']
        return full_path

    def find_files_in_dir(self, username, path, d):
        for files in mongo.file_collection.find({'username': username, 'path': path}):
            d.append(files['name'])
        return d
