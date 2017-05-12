# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "..")

from ctrip import ctripCrawler
import models
import time

def start(page):
	maxPage = 550
	_page = page

	if _page < maxPage:
		_ctrip = ctripCrawler.getModule('sanya61/3420335')

		_ids = _ctrip.getListForPage(_page)

		print 'start: 第' + str(_page) + '页数据开始保存 ============='	

		for _id in _ids:
			obj = ctripCrawler.getModule(_id)
			result = models.saveArticle(obj, _id)

			if result:
				if result['_id']:
					print 'saving: 保存第' + str(_page) + '页，_id为：' + str(_id) + '，数据保存成功'
				else:
					print 'saving: 保存第' + str(_page) + '页，_id为：' + str(_id)	+ '，已有相关数据'

				if result['isQuery'] is 'true':
					time.sleep(6)	
			else:
				print 'saving: 保存第' + str(_page) + '页，_id为：' + str(_id) + '，数据保存失败'			

		print 'end: 第' + str(_page) + '页数据保存成功 ============='

		_page += 1;

		start(_page);
		time.sleep(6)

	else:
		print 'warning: 页数不能超过'+ str(maxPage) +' ============='	

start(32)
	


		