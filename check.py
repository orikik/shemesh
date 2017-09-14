import os

import shutil

import mongo
from directories.dir_db import DB_dir


#print(os.getcwd())
#os.mkdir(path = 'C:/work/shemesh/tests/tet')
#os.rmdir(path= 'C:/work/shemesh/tests/text')
data = {
        'username': 'testing',
        'password': '1234'
    }
params_file = {
    'username':'orik',
    'path':'C:/фотки/example.txt',
    'file_format':'.txt'
}
path_to = ''

for men in mongo.collection.find():
    print(men)
for men in mongo.file_collection.find():
    print(men)
for men in mongo.dev_collection.find():
    print(men)
for men in mongo.dir_collection.find():
    print(men)


