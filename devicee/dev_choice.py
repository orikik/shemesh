import os

from devicee.device_manager import choose_device
from devicee.exchange import Exchange
from devicee.path_manager import create_path

from devicee.DB_manager import DB


class Dev:
    def __init__(self):
        pass

    def add_file(self, username, user_path, storage_path=''):
        size = os.path.getsize(user_path)
        name = os.path.basename(user_path)
        dev_path = choose_device()
        dir_path = create_path(dev_path=dev_path, username=username, path_to=storage_path)
        if os.path.isfile(user_path):
            f = DB().dev_size_find(dev_path=dev_path)
            if f >= size:
                if not DB().file_exist(username=username, dir_path=dir_path, name=name):
                    Exchange().send_file(user_path=user_path, storage_main_path=dev_path + dir_path)
                    DB().update_device(size=size, dev_path=dev_path)
                    params_file = {
                        'username': username,
                        'device': dev_path,
                        'path': dir_path,
                        'size': size,
                        'name': name
                    }
                    DB().update_files(params_file)
                    return 'A new file added.'
                else:
                    return 'A file with this name already exists.'
            else:
                return 'All devices are full.'
        else:
            return 'Specify the full path.'

    def remove_file(self, username, name, storage_path=''):
        path = '/' + username + '/' + storage_path
        file = DB().get_file(username=username, name=name, dir_path=path)
        if file:
            os.remove(file['device']+file['path']+file['name'])
            DB().remove_file(file)
            size = file['size']
            DB().update_device(size=-size, dev_path=file['device'])
            return 'file delete'
        else:
            return 'file does not exist.'

    def update_file(self, username, user_path, storage_path=''):
        name = os.path.basename(user_path)
        path = '/' + username + '/' + storage_path
        file = DB().get_file(username=username, name=name, dir_path=path)
        if os.path.isfile(user_path):
            if file:
                self.remove_file(username=username, name=name, storage_path=storage_path)
                self.add_file(username=username, user_path=user_path, storage_path=storage_path)
                return 'File update.'
            else:
                return 'File does not exist.'
        else:
            return 'Specify the full path.'

    def get_file(self, username, user_path, name, storage_path=''):
        path = '/' + username + '/' + storage_path
        file = DB().get_file(username=username, name=name, dir_path=path)
        if file:
            full_path = file['device'] + file['path'] + file['name']
            Exchange().get_file(user_path=user_path, storage_main_path=full_path)
            return 'File download.'
        else:
            return 'A file with this name does not exists.'

