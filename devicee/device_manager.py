import mongo
from devicee.DB_manager import DB


def choose_device():
    space = 0
    for men in mongo.dev_collection.find():
        if men['free space'] > space:
            space = men['free space']
    dev = DB().get_device(space)
    return dev['path']
