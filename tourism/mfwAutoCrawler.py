# -*- coding: utf-8 -*-

from mafengwo import mfwCrawler
import models
import time

def start(page):
	maxPage = 20
	_page = page

	if _page < maxPage:
		_mafengwo = mfwCrawler.getMaFengWo('6899663')

		_ids = _mafengwo.getListForPage(_page)

		print 'start: 第' + str(_page) + '页数据开始保存 ============='	

		for _id in _ids:
			obj = mfwCrawler.getMaFengWo(_id)
			result = models.saveArticle(obj, _id)

			if result:
				if result['_id']:
					print 'saving: 保存第' + str(_page) + '页，_id为：' + str(_id) + '，数据保存成功'
				else:
					print 'saving: 保存第' + str(_page) + '页，_id为：' + str(_id)	+ '，已有相关数据'
			else:
				print 'saving: 保存第' + str(_page) + '页，_id为：' + str(_id) + '，数据保存失败'			

			time.sleep(10)

		print 'end: 第' + str(_page) + '页数据保存成功 ============='

		_page += 1;

		start(_page);

	else:
		print 'warning: 页数不能超过'+ str(maxPage) +' ============='	

start(1)
	


		