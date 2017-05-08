# -*- coding: utf-8 -*-

from pymongo import MongoClient
import settings

#连接
client=MongoClient('mongodb://127.0.0.1:27017/')

db = client[settings.DBNAME]

def getCollection(collection):
	if(collection):
		return db[collection]
	else:
		return None	
