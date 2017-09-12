from director.directorys import Dir


class Correct:
    def add_dir(self, data, username):
        key1 = 'path' in data
        key2 = 'name' in data
        if key1 and key2 and len(data) == 2:
            n = Dir(username=username, path_to=data['path'], name=data['name']).new_directory()
            return n
        elif key2 and len(data) == 1:
            n = Dir(username=username, name=data['name']).new_directory()
            return n
        else:
            return 'Incorrect data', 400

    def remove_dir(self, data, username):
        key1 = 'path' in data
        key2 = 'name' in data
        if key1 and key2 and len(data) == 2:
            n = Dir(username=username, path_to=data['path'], name=data['name']).remove_directory()
            return n
        elif key2 and len(data) == 1:
            n = Dir(username=username, name=data['name']).remove_directory()
            return n
        else:
            return 'Incorrect data', 400

    def change_name(self, data, username):
        key1 = 'old_name' in data
        key2 = 'new_name' in data
        key3 = 'path' in data
        if key1 and key2 and key3 and len(data) == 3:
            n = Dir(username=username, path_to=data['path'], name=data['old_name']).change_name_directory(data['new_name'])
            return n
        elif key1 and key2 and len(data) == 2:
            n = Dir(username=username, name=data['old_name']).change_name_directory(data['new_name'])
            return n
        else:
            return 'Incorrect data', 400

    def get_list(self, data, username):
        key1 = 'path' in data
        key2 = 'name' in data
        if key1 and key2 and len(data) == 2:
            n = Dir(username=username, path_to=data['path'], name=data['name']).getting_a_list_of_directory_files()
            return n
        elif key2 and len(data) == 1:
            n = Dir(username=username, name=data['name']).getting_a_list_of_directory_files()
            return n
        else:
            return 'Incorrect data', 400
