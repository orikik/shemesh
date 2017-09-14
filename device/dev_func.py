import os
from device.device_manager import choose_device
from device.exchange import Exchange
from device.path_manager import Path
from device.DB_manager import DB


class Dev:
    def add_file(self, username, user_path, storage_path=''):
        dev_path = choose_device()
        dir_path = Path().create_path(dev_path=dev_path, username=username, path_to=storage_path)
        if os.path.isfile(user_path):
            size = os.path.getsize(user_path)
            name = os.path.basename(user_path)
            f = DB().dev_size_find(dev_path=dev_path)
            if f >= size:
                if not DB().file_exist(username=username, dir_path=dir_path, name=name):
                    DB().update_device(size=size, dev_path=dev_path)
                    params_file = {
                        'username': username,
                        'device': dev_path,
                        'path': dir_path,
                        'size': size,
                        'name': name
                    }
                    DB().update_files(params_file)
                    f = Exchange().send_file(user_path=user_path, storage_main_path=dev_path + '/' + dir_path)
                    return f
                else:
                    return 'A file with this name already exists.', 403
            else:
                return 'All devices are full.', 413
        else:
            return 'Specify the full path.', 404

    def remove_file(self, username, name, storage_path=''):
        if storage_path == '':
            path = username
        else:
            path = username + '/' + storage_path
        file = DB().get_file(username=username, name=name, dir_path=path)
        if file:
            Exchange().remove_file(file['device'] + '/' + file['path'] + '/' +file['name'])
            DB().remove_file(file=file)
            return 'file delete'
        else:
            return 'file does not exist.', 404

    def update_file(self, username, user_path, storage_path=''):
        name = os.path.basename(user_path)
        path = username + '/' + storage_path
        file = DB().get_file(username=username, name=name, dir_path=path)
        if os.path.isfile(user_path):
            if file:
                self.remove_file(username=username, name=name, storage_path=storage_path)
                self.add_file(username=username, user_path=user_path, storage_path=storage_path)
                return 'File update.'
            else:
                return 'File does not exist.', 404
        else:
            return 'Specify the full path.', 404

    def get_file(self, username, user_path, name, storage_path=''):
        path = username + '/' + storage_path
        file = DB().get_file(username=username, name=name, dir_path=path)
        if file:
            full_path = file['device'] + '/' + file['path'] + '/' + file['name']
            Exchange().get_file(user_path=user_path, storage_main_path=full_path)
            return 'File download.'
        else:
            return 'A file with this name does not exists.', 404

