import mongo


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
for men in mongo.collection.find():
    print(men['_id'])
for men in mongo.file_collection.find():
    print(men)
for men in mongo.dev_collection.find():
    print(men)
for men in mongo.dir_collection.find():
    print(men)
