import pymongo
import os


con_str = "mongodb+srv://{0}:{1}@{2}/{3}?retryWrites=true&w=majority".format(
    os.getenv("MONGO_USER"),
    os.getenv("MONGO_PASSWORD"),
    os.getenv("MONGO_SERVER"),
    os.getenv("MONGO_DB"),
)

client = pymongo.MongoClient(con_str)