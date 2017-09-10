from director.dir_db import DB_dir
from director.remove_tree_in_device import remove_tree
from device.dev_func import Dev
from device.DB_manager import DB


class Dir:
    def __init__(self, username, name, path_to=''):
        self.username = username
        self.name = name
        self.path_to = path_to
        self.path_one = username + '/' + name
        if self.path_to == '':
            self.dir_path = username
            self.full_path = username + '/' + name
            self.f = True
        else:
            self.dir_path = username+'/' + path_to
            self.full_path = username+'/'+path_to + '/' + name
            self.f = DB_dir().path_to_dir_exist(username=self.username, dir_path=self.dir_path)
        self.similar = DB_dir().dir_exist(username=self.username, name=self.name, full_path=self.full_path)

    def new_directory(self):
        if not self.similar:
            if self.f:
                n = DB_dir().add_dir(username=self.username, name=self.name, full_path=self.full_path)
                return n
            else:
                return 'This path does not exist.'
        else:
            return 'A directory with this name already exists.'

    def change_name_directory(self, new_name):
        if self.similar:
            if not DB_dir().dir_exist(username=self.username, name=self.name, full_path=self.dir_path + '/' + new_name):
                n = DB_dir().dir_update(new_name=new_name, full_path=self.full_path)
                return n
            else:
                return 'A directory with this name already exists.'
        else:
            return 'A directory named "' + self.name + '" does not exist.'

    def remove_directory(self):
        if self.similar:
            n = self.getting_a_list_of_directory_files()
            if len(n) != 0:
                for m in n:
                    Dev().remove_file(username=self.username, name=m, storage_path=self.path_to)
                for v in DB().all_dev():
                    path = v['path'] + '/' + self.similar['full path']
                    remove_tree(path=path)
            n = DB_dir().remove_dir(self.similar)
            return n
        else:
            return 'A directory named \"' + self.name + '\" does not exist.'

    def getting_a_list_of_directory_files(self):
        if self.similar:
            d = []
            n = DB_dir().find_files_in_dir(username=self.username, path=self.full_path, d=d)
            if len(n) == 0:
                return 'Directory is empty.'
            else:
                return d
        else:
            return 'A directory named \"' + self.name + '\" does not exist.'


