from curses.ascii import NUL
from http import client
from sqlite3 import dbapi2
from pymongo import MongoClient
import json, pymongo

class mongodbconnector:

    def __init__(self, hostPort, username, password, queryParam, databaseName, isCloud):
        
        if(isCloud):
            protocol="mongodb+srv"
        else:
            protocol="mongodb"

        connectionString=protocol + "://"

        if(username):
            connectionString = connectionString + username + ":" + password + "@"
        
        connectionString = connectionString + hostPort + queryParam

        self.client = MongoClient(connectionString)
        self.db = self.client[databaseName]

    def getCollectionNames(self):
        for name in self.db.list_collection_names():
            print("DB collection list:")
            print(name)
            print ("===================")

    def insertintoSample(self, content):
        sampleCollection = self.db['sampleCollection']
        result = sampleCollection.insert_one(content)
        return result

    def getAllSampleCollection(self):
         sampleCollections = self.db['sampleCollection']
         return list(sampleCollections.find())

    def deleteSample(self, _id):
        sampleCollections = self.db['sampleCollection']
        myquery = { "_id": _id.inserted_id  }
        sampleCollections.delete_one(myquery)

    def UpdateSample(self, data, _id):
        sampleCollections = self.db['sampleCollection']
        query = {'_id': _id.inserted_id }
        result = sampleCollections.replace_one(query, data, upsert=True)
        return result