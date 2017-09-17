import mongo


for men in mongo.collection.find():
    print(men)
for men in mongo.file_collection.find():
    print(men)
for men in mongo.dev_collection.find():
    print(men)
for men in mongo.dir_collection.find():
    print(men)


