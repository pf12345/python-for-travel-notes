# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import time

from bson.objectid import ObjectId


##携程游记
class CTRIP:
	#初始化，传入基地址，是否只看楼主的参数
	def __init__(self,article_id):
		self.baseURL = 'http://you.ctrip.com/travels/' + article_id + '.html'
		self.userInfoURL = 'https://www.mafengwo.cn/note/__pagelet__/pagelet/headOperateApi?callback=jQuery1810173556954190627_1492868085919&params=%7B%22iid%22%3A%22' + article_id +'%22%7D&_=1492868086249'
		self.defaultTitle = '美好游记'
		self.oldIds = []
		self.soup = None

	
	def getPage(self):
		try:
			if self.soup:
				return self.soup
			else:	
				url = self.baseURL
				request = urllib2.Request(url)
				response = urllib2.urlopen(request)
				_html = response.read().decode('utf8').encode('utf8')
				pattern1 = re.compile('\&nbsp\;')
				_html = re.sub(pattern1, " ", _html)
				soup = BeautifulSoup(_html, "html.parser")
				self.soup = soup
				return soup
		except Exception, e:
			if hasattr(e,"reason"):
				print u"连接失败,错误原因",e.reason
				return None

	def getTitle(self):
		soup = self.getPage()
		if soup and soup.select('.title1'):
			return soup.select('.title1')[0].string
		else:
			return ''	

	def getContent(self):
		soup = self.getPage()
		if soup and soup.select('.ctd_content'):
			article = soup.select('.ctd_content')[0]
			images = article.select('.img_blk img')
			links = article.select('a')
			firstImg = ''

			if soup.select('.ctd_imgbox img'):
				firstImg = soup.select('.ctd_imgbox img')[0]['src']

			articleText = ''

			for link in links:
				link['href'] = 'javascript:;'

			for img in images:
				if not firstImg:
					firstImg = img['src']
				img['src'] = img['data-original']	

			for item in article.stripped_strings:
				articleText += item

			return {"html": article.prettify(), "text": articleText, "firstImg": firstImg}	
		else:
			return {"html": '', "text": '', "firstImg": ''}
	

	def getUser(self):
		soup = self.getPage()
		if soup:
			if soup.select('.user_img img'):
				avatar = soup.select('.user_img img')[0]['src']
			else:
				avatar = ''	
			if soup.select('.nickname'):	
				name = soup.select('.nickname a')[0].string.encode('utf-8')
			else:
				name = ''	
			if soup.select('.time'):
				_time = soup.select('.time')[0].string	
			else:
				_time = ''	

			return {"name": name, "avatar": avatar, "oldCreated": _time}	
		else:
			return {"name": '', "avatar": '', "oldCreated": ''}


	def getWebsite(self):

		return {"url": self.baseURL, "name": "携程"}


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

def getCtrip(id):
	return CTRIP(id)

# ctrip = CTRIP('sanya61/3420335')

# print ctrip.getTitle()
# print ctrip.getContent()
# print ctrip.getUser()
