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
path_to = ''
for men in mongo.collection.find():
    print(men)
for men in mongo.file_collection.find():
    print(men)
for men in mongo.dev_collection.find():
    print(men)
for men in mongo.dir_collection.find():
    m = len(men['full path'].split('/')) - 1
    for n in range(1, m):
        if n == 1:
            path_to = path_to + 'plomba_0' + '/'
        else:
            path_to = path_to + men['path' + str(n)] + '/'
    full_path = men['username'] + '/' + path_to + men['name']
    path_to = ''
    print(full_path)
    print(men)

