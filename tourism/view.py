# -*- coding: utf-8 -*-
#from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from models import getCollection
import datetime
import pprint
import json
import sys
from bson.objectid import ObjectId
from bson.json_util import dumps
 
import mafengwo
import tripadvisor

def list(request):
	return render(request, 'list.html')

def getList(request):
	articleCollection = getCollection('tourism')
	articles = articleCollection.find()

	_articles = []
	for article in articles:
		_article = {
			"title": article['title'],
			"content_txt": article['content_txt'],
			"firstImg": article['firstImg'],
			"user": article['user'],
			"site": article['site'],
			"_id": str(article['_id'])
		}
		_articles.append(_article)

	return HttpResponse(json.dumps({"result": "ok", "data": _articles}), content_type="application/json")

def getMafengwoIds(request):
	_mafengwo = mafengwo.getMaFengWo('6899663')

	_mafengwo.getListForPage(6)	

	# print _mafengwo.getIds()
	_ids = ''

	for item in _mafengwo.getIds():
		_ids += '    '
		_ids += item

	return HttpResponse(_ids)


# 保存马蜂窝游记请求
def saveMafengwo(request, id):
	_id = id

	_mafengwo = mafengwo.getMaFengWo(_id)

	result = saveArticle(_mafengwo, _id)

	return HttpResponse(json.dumps(result))


# 保存tripAdvu=isor(官方中文名 猫途鹰)游记请求
def saveTripAdvisor(request, id):
	
	_id = id

	_tripAdvisor = tripadvisor.getTripAdvisor(_id)

	result = saveArticle(_tripAdvisor, _id)

	return HttpResponse(json.dumps(result))

# 游记详情
def detail(request, _id):
	if _id:
		articleCollection = getCollection('tourism')
		article = articleCollection.find_one({"_id": ObjectId(_id)})
		return render(request, 'detail.html', article)
	else:
		return HttpResponse('未找到相应数据')	

# 公用，保存游记进入数据库接口
def saveArticle(obj, id):

	articleCollection = getCollection('tourism')
	if articleCollection.find_one({"oldId": id}):
		return {"_id": None, "message": "已有相关数据"}

	title = obj.getTitle()

	article = obj.getContent()

	user = obj.getUser()

	site = obj.getWebsite()

	if article['html'] is '':
		return {"_id": None, "message": "内容为空"}

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
		"oldCreated": user['oldCreated']
	}

	tourismCollection = getCollection('tourism')
	_id = tourismCollection.insert_one(tourism).inserted_id

	# print _id['_id']
	print str(_id)

	return {"_id": str(_id), "message": "保存成功"}
