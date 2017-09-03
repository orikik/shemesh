
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.sampleDB

collection = db.dataset
file_collection = db.user
dev_collection = db.dev
dir_collection = db.dir

api_url = "http://127.0.0.1:5000/"
