import os
from director.dir_db import DB_dir


def create_path(dev_path, username, path_to=''):
    m = dev_path
    n = "/" + username + '/' + path_to
    if path_exist(dev_path, username, path_to):
        return n
    else:
        os.mkdir(path=m + n)
        return n


def path_exist(dev_path, username, path_to=''):
    m = dev_path
    n = "/" + username + '/' + path_to
    if path_to != '':
        if os.path.exists(m + n) and DB_dir().dir_exists(username=username, full_path=n):
            return True
    else:
        if os.path.exists(m + n):
            return True
