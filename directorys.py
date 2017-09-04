import os

import mongo
from devicee.dev_choice import Dev


class Dir:
    def __init__(self, username, name, path_to=''):
        self.username = username
        self.name = name
        self.path_to = path_to
        self.path_one = username+'/'+name
        self.dir_path = username+'/' + path_to
        self.full_path = username+'/'+path_to+'/'+name
        self.similar = mongo.dir_collection.find_one({'username': username, 'name': name, 'full path': self.full_path})
        self.f = mongo.dir_collection.find_one({'username': username, 'full path': self.dir_path})

    def new_directory(self):
        if not self.similar:
            if self.f or self.path_to == '':
                if self.path_to == '':
                    params = {
                        'username': self.username,
                        'name': self.name,
                        'full path': self.path_one
                    }
                else:
                    params = {
                        'username': self.username,
                        'name': self.name,
                        'full path': self.full_path
                    }
                mongo.dir_collection.save(params)
                return 'A new directory created.'
            else:
                return 'This path does not exist.'
        else:
            return 'A directory with this name already exists.'

    def change_name_directory(self, new_name):
        if self.similar:
            mongo.dir_collection.update(self.f, {'name':new_name})
            return 'The directory name has been changed.'
        else:
            return 'A directory named "' + self.name + '" does not exist.'

    def remove_directory(self):
        if self.similar:
            n = self.getting_a_list_of_directory_files()
            if len(n) != 0:
                for m in n:
                    Dev().remove_file(username=self.username, name=m, storage_path=self.path_to)
                for v in mongo.dev_collection.find():
                    path = v['path'] + '/' + self.similar['full path']
                    os.removedirs(path=path)
            mongo.dir_collection.remove(self.f)
            return 'The directory was deleted.'
        else:
            return 'A directory named \"' + self.name + '\" does not exist.'

    def getting_a_list_of_directory_files(self):
        if self.similar:
            d = []
            for files in mongo.file_collection.find({'username':self.username, 'path':("/" + self.username + "/" + self.path_to + self.name)}):
                d.append(files['name'])
            if len(d) == 0:
                return 'Directory is empty.'
            else:
                return d
        else:
            return 'A directory named \"' + self.name + '\" does not exist.'


