from device.dev_func import Dev


class Correct:
    def add(self, data, username):
        key1 = 'my path' in data
        key2 = 'storage path' in data
        if key1 and key2 and len(data) == 2:
            n = Dev().add_file(username=username, user_path=data['my path'], storage_path=data['storage path'])
            return n
        elif key1 and len(data) == 1:
            n = Dev().add_file(username=username, user_path=data['my path'])
            return n
        else:
            return 'Incorrect data.'

    def remove(self, data, username):
        key1 = 'storage path' in data
        key2 = 'name' in data
        if key1 and key2 and len(data) == 2:
            n = Dev().remove_file(username=username, name=data['name'], storage_path=data['storage path'])
            return n
        elif key2 and len(data) == 1:
            n = Dev().remove_file(username=username, name=data['name'])
            return n
        else:
            return 'Incorrect data.'

    def update(self, data, username):
        key1 = 'my path' in data
        key2 = 'storage path' in data
        if key1 and key2 and len(data) == 2:
            n = Dev().update_file(username=username, storage_path=data['storage path'], user_path=data['my path'])
            return n
        elif key1 and len(data) == 1:
            n = Dev().update_file(username=username, user_path=data['my path'])
            return n
        else:
            return 'Incorrect data.'

    def get(self, data, username):
        key1 = 'name' in data
        key2 = 'my path' in data
        key3 = 'storage path' in data
        if key1 and key2 and key3 and len(data) == 3:
            n = Dev().get_file(username=username, user_path=data['my path'],storage_path=data['storage path'], name=data['name'])
            return n
        elif key1 and key2 and len(data) == 2:
            n = Dev().get_file(username=username, user_path=data['my path'], name=data['name'])
            return n
        else:
            return 'Incorrect data.'
