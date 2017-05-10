# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
import models
import json
from bson.objectid import ObjectId
 
from mafengwo import mfwCrawler
from tripadvisor import tripadvisorCrawler
from ctrip import ctripCrawler

def list(request):
	return render(request, 'list.html')

#获取游记列表接口
def getList(request):
	articleCollection = models.getCollection('tourism')
	articles = articleCollection.find().limit(20)

	_articles = []
	for article in articles:
		_article = {
			"title": article['title'],
			"firstImg": article['firstImg'],
			"user": article['user'],
			"site": article['site'],
			"_id": str(article['_id'])
		}
		_articles.append(_article)

	return HttpResponse(json.dumps({"result": "ok", "data": _articles}), content_type="application/json")


# 保存单篇马蜂窝游记请求
def saveMafengwo(request, id):
	_id = id

	_mafengwo = mfwCrawler.getMaFengWo(_id)

	result = models.saveArticle(_mafengwo, _id)

	return HttpResponse(json.dumps(result))


# 保存tripAdvu=isor(官方中文名 猫途鹰)游记请求
def saveTripAdvisor(request, id):
	_id = id

	_tripAdvisor = tripadvisorCrawler.getTripAdvisor(_id)

	result = models.saveArticle(_tripAdvisor, _id)

	return HttpResponse(json.dumps(result))

# 保存tripAdvu=isor(官方中文名 猫途鹰)游记请求
def saveCtrip(request):

	_id = 'sanya61/3420335'
	
	_ctrip = ctripCrawler.getCtrip('sanya61/3420335')

	result = models.saveArticle(_ctrip, _id)

	return HttpResponse(json.dumps(result))	


# 游记详情
def detail(request, _id):
	if _id:
		articleCollection = models.getCollection('tourism')
		article = articleCollection.find_one({"_id": ObjectId(_id)})
		return render(request, 'detail.html', article)
	else:
		return HttpResponse('未找到相应数据')	
