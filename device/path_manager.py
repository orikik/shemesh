import os
from device.DB_manager import DB


class Path:
    def create_path(self, dev_path, username, path_to=''):
        m = dev_path
        if path_to == '':
            n = username
        else:
            n = username + '/' + path_to
        if self.path_exist(dev_path, username, path_to):
            return n
        else:
            os.makedirs(m + '/' + n)
            return n

    def path_exist(self, dev_path, username, path_to=''):
        m = dev_path
        n = username + '/' + path_to
        if path_to != '':
            if os.path.exists(m + '/' + n) and DB().dir_exists(username=username, full_path=n):
                return True
        else:
            if os.path.exists(m + '/' + n):
                return True

    def change_name_dir(self, dev, old_full_path, new_full_path):
        m = dev
        if os.path.exists(m + old_full_path):
            os.renames(m + old_full_path, m + new_full_path)

    def full_path_exist(self, dev, full_path):
        if os.path.exists(dev + '/' + full_path):
            return True
