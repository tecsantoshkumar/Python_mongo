import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["electrotech"]
mycol = mydb["user"]

for x in mycol.find({},{ "id": 1, "name":1, "videos":1}):
  print(x)