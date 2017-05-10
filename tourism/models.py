# -*- coding: utf-8 -*-

from pymongo import MongoClient
import settings
import datetime

#连接
client=MongoClient('mongodb://127.0.0.1:27017/')

db = client[settings.DBNAME]

def getCollection(collection):
	if(collection):
		return db[collection]
	else:
		return None	


#保存游记入数据库
def saveArticle(obj, id):
	articleCollection = getCollection('tourism')
	if articleCollection.find_one({"oldId": id}):
		return {"_id": None, "message": "已有相关数据", "isQuery": "false"}

	title = obj.getTitle()

	article = obj.getContent()

	user = obj.getUser()

	site = obj.getWebsite()

	if article['html'] is '':
		return {"_id": None, "message": "内容为空", "isQuery": "true"}	

	tourism = {
		"title": title,
		"content": article['html'],
		"content_txt": article['text'],
		"firstImg": article['firstImg'],
		"created": datetime.datetime.today().strftime( '%Y-%m-%d %H:%M:%S'),
		"updated": datetime.datetime.now().strftime( '%Y-%m-%d %H:%M:%S'),
		"user": user,
		"site": site,
		"oldId": id,
		"oldCreated": ''
	}

	if user and user['oldCreated']:
		tourism['oldCreated'] = user['oldCreated']

	tourismCollection = getCollection('tourism')
	_id = tourismCollection.insert_one(tourism).inserted_id

	return {"_id": str(_id), "message": "保存成功", "_title": title, "isQuery": "true"}		
