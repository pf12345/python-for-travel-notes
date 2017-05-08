# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup

#汽车之家，自驾游爬虫类
class BDTB:
	#初始化，传入基地址，是否只看楼主的参数
	def __init__(self,baseUrl_left,baseUrl_right):
		self.baseURL_left = baseUrl_left
		self.baseURL_right = baseUrl_right
		self.defaultTitle = '汽车之家，自驾游记'
	#传入页码，获取该页帖子的代码
	def getPage(self,pageNum):
		try:
			url = self.baseURL_left + str(pageNum) + self.baseURL_right
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			soup = BeautifulSoup(response.read().decode('gbk').encode('utf8'))
			return soup
		except urllib2.URLError, e:
			if hasattr(e,"reason"):
				print u"连接汽车之家，自驾游失败,错误原因",e.reason
				return None
	def gtitle(self):
		soup = self.getPage(1)
		if not soup:
			return None
		if not soup.select('.maxtitle') or not soup.select('.maxtitle')[0]:
			return None
		else:
			return soup.select('.maxtitle')[0].string
	def getContent(self):
		soup = self.getPage(1)
		if not soup:
			return None
		contents = soup.find_all("div", class_="w740")	
		return 	contents




def pach():
	baseURL_left = 'http://club.autohome.com.cn/bbs/threadowner-c-200042-62195152-'
	baseURL_right = '.html#pvareaid=101435'
	bdtb = BDTB(baseURL_left, baseURL_right)
	return bdtb.getContent()
# bdtb.getPage(1)
# print bdtb.gtitle()
# bdtb.getContent()

