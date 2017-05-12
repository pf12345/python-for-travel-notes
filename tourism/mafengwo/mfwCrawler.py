# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import time

from bson.objectid import ObjectId



class MAFENGWO:
	#初始化，传入基地址，是否只看楼主的参数
	def __init__(self,article_id):
		self.baseURL = 'https://www.mafengwo.cn/i/' + article_id + '.html'
		self.userInfoURL = 'https://www.mafengwo.cn/note/__pagelet__/pagelet/headOperateApi?callback=jQuery1810173556954190627_1492868085919&params=%7B%22iid%22%3A%22' + article_id +'%22%7D&_=1492868086249'
		self.defaultTitle = '美好游记'
		self.oldIds = []

	
	def getPage(self):
		try:
			url = self.baseURL
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			soup = BeautifulSoup(response.read().decode('utf8').encode('utf8'), "html.parser")
			return soup
		except Exception, e:
			if hasattr(e,"reason"):
				print u"连接失败,错误原因",e.reason
				return None

	def getTitle(self):
		soup = self.getPage()
		if soup and soup.select('.headtext'):
			return soup.select('.headtext')[0].string
		else:
			return ''	

	def getContent(self):
		soup = self.getPage()
		if soup and soup.select('.vc_article'):
			article = soup.select('.vc_article')[0]
			images = article.select('._j_lazyload')
			links = article.select('a')
			firstImg = ''

			if soup.select('._j_load_cover img'):
				firstImg = soup.select('._j_load_cover img')[0]['src']

			for s in soup.select('.vc_total'):
				s.extract()

			articleText = ''

			for link in links:
				link['href'] = 'javascript:;'

			for img in images:
				if not firstImg:
					firstImg = img['data-src']
				img['src'] = img['data-src']

			for item in article.stripped_strings:
				articleText += item

			return {"html": article.prettify(), "text": articleText, "firstImg": firstImg}	
		else:
			return {"html": '', "text": '', "firstImg": ''}


	def removeJqueryJson(self, url):

		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		result = response.read()

		pattern = re.compile('jQuery.*?\(')
		pattern1 = re.compile('\)\;')

		result = re.sub(pattern, "", result)
		result = re.sub(pattern1, "", result)

		result = eval(result)

		html = result['data']['html']

		return html		

	def getUser(self):
		try:
			url = self.userInfoURL

			html = self.removeJqueryJson(url)

			soup = BeautifulSoup(html, "html.parser")	

			if soup:	
				if soup.select('.per_pic img'):
					avatar = soup.select('.per_pic img')[0]['src']
				else:
					avatar = ''	

				if soup.select('.per_name'):	
					name = soup.select('.per_name')[0]['title'].encode('utf-8')
				else:
					name = ''	

				if soup.select('.time'):
					_time = ''
					time = soup.select('.time')[0].stripped_strings
					for item in time:
						if not _time:
							_time = item

					pattern2 = re.compile('<.*?span>', re.S)
					_time = re.sub(pattern2, "", _time)
				else:
					_time = ''

				return {"name": name, "avatar": avatar, "oldCreated": _time}
			else:
				
				return {"name": '', "avatar": '', "oldCreated": ''}

		except Exception, e:
			if hasattr(e,"reason"):
				print u"连接失败,错误原因",e.reason
				return {"name": '', "avatar": '', "oldCreated": ''}

	

	def getWebsite(self):

		return {"url": self.baseURL, "name": "蚂蜂窝"}


	def getListForPage(self, page):

		if page < 250:

			url = 'http://www.mafengwo.cn/note/__pagelet__/pagelet/recommendNoteApi?callback=jQuery18103478581123017468_1492999122522&params=%7B%22type%22%3A0%2C%22objid%22%3A0%2C%22page%22%3A'+str(page)+'%2C%22ajax%22%3A1%2C%22retina%22%3A0%7D&_=1492999206862'	

			try:

				html = self.removeJqueryJson(url)

				html = html.replace('\\/', '/')

				html = html.decode('string-escape')

				soup = BeautifulSoup(html, "html.parser")		

				links = soup.select('.tn-item .tn-image a')

				index = 0

				_ids = []

				for link in links:
					_id = link['href'].replace('/i/', '').replace('.html', '')

					_ids.append(_id)

				return _ids

			except Exception, e:
				if hasattr(e,"reason"):
					print u"连接失败,错误原因",e.reason
					return None	


	def getIds(self):
		return 	self.oldIds			

def getModule(id):
	return MAFENGWO(id)


