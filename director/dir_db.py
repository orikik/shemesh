import mongo
from device.DB_manager import DB
from device.path_manager import Path


class DB_dir:
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

    def get_dir(self, username, name, full_path):
        n = mongo.dir_collection.find_one({'username': username, 'name': name, 'full path': full_path})
        return n

    def remove_dir(self, data):
        m = str(len(data['full path'].split('/'))-1)
        for dir in mongo.dir_collection.find({'path'+m:data['name']}):
            for file in mongo.file_collection.find({'path':dir['full path']}):
                DB().remove_file(file)
            mongo.dir_collection.remove(dir)
        for file in mongo.file_collection.find({'path':data['full path']}):
            DB().remove_file(file)
        mongo.dir_collection.remove(data)
        return 'The directory was deleted.'

    def dir_update(self, new_name, full_path):
        n = mongo.dir_collection.find_one({'full path':full_path})
        old_full_path = n['full path']
        m = str(len(full_path.split('/'))-1)
        for path in mongo.dir_collection.find({'path' + m: n['name']}):
            list = path['full path'].split('/')
            list[int(m)] = new_name
            new_full_path = '/'.join(list)
            mongo.dir_collection.update(path, {"$set": {"path" + m: new_name, 'full path': new_full_path}})
        list = n['full path'].split('/')
        list[-1] = new_name
        new_full_path = '/'.join(list)
        mongo.dir_collection.update(n, {"$set": {'name': new_name, 'full path': new_full_path}})
        for dev in mongo.dev_collection.find():
            Path().change_name_dir(dev=dev['path'], old_full_path=old_full_path, new_full_path=new_full_path)
        return 'The directory name has been changed.'

    def find_files_in_dir(self, username, path):
        d = []
        for files in mongo.file_collection.find({'username': username, 'path': path}):
            d.append(files['name'])
        return d
