# -*- coding: utf-8 -*-
import pymongo
from common import config

class Mongo():
    def __init__(self):
        hostMongo  = config()['mongo']['host']
        db = config()['mongo']['db']
        collection  = config()['mongo']['collection']        
        connection = pymongo.MongoClient(hostMongo, connect=False, maxPoolSize=None)
        self.db = connection[db][collection]

    def insert(self, data):
        inserted = self.db.insert_one(data)
        if inserted:
            print("Inserted")
        else:
            print("Not inserted")

    def insertMany(self, data):
        inserted = self.db.insert_many(data)
        if inserted:
            print("Inserted")
        else:
            print("Not inserted")