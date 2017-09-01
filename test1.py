import mongo

mongo.collection.remove({})
mongo.file_collection.remove({})
mongo.dev_collection.remove({})


dev_0 = {
    'path':'C:/dev_0',
    'name':'dev_0',
    'free space': 1000000,
    'used space': 0
}
dev_1 = {
    'path':'C:/dev_1',
    'name':'dev_1',
    'free space': 1000000,
    'used space': 0
}
dev_2 = {
    'path':'C:/dev_2',
    'name':'dev_2',
    'free space': 1000000,
    'used space': 0
}
mongo.dev_collection.save(dev_0)
mongo.dev_collection.save(dev_1)
mongo.dev_collection.save(dev_2)