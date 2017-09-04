import mongo


def dir_exists(username, full_path):
    if mongo.dir_collection.find_one({'username': username, 'full path': full_path}):
        return True
    else:
        return False
