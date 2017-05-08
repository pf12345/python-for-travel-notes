# -*- coding:utf-8 -*-
import urllib
import urllib2
import re


#处理页面标签类
class Tool:
	#删除style
	removeStyle = re.compile('<style.*?>.*?</style>')
	#删除script
	removeScript = re.compile('<script.*?>.*?</script>')
	removeSrc = re.compile('src="http://x.autoimg.cn/club/lazyload.png"')
	removeOnload = re.compile('onload="(.*?)"')
	removeOnerror = re.compile('onerror="(.*?)"')
	removeUl = re.compile('<ul>.*?</ul>')
	removeColor = re.compile('<span.*?COLOR.*?>.*?</span>')
	replaceSrc9 = re.compile('src9')
	def replace(self, x):
		x = re.sub(self.removeStyle, "", x)
		x = re.sub(self.removeScript, "", x)
		x = re.sub(self.removeSrc, "", x)
		x = re.sub(self.removeOnload, "", x)
		x = re.sub(self.removeOnerror, "", x)
		x = re.sub(self.removeUl, "", x)
		x = re.sub(self.removeColor, "", x)
		x = re.sub(self.replaceSrc9, "src", x)
		return x.strip()


#汽车之家，自驾游爬虫类
class BDTB:
	#初始化，传入基地址，是否只看楼主的参数
	def __init__(self,baseUrl_left,baseUrl_right):
		self.baseURL_left = baseUrl_left
		self.baseURL_right = baseUrl_right
		self.tool = Tool()
		self.defaultTitle = '汽车之家，自驾游记'
		self.file = None
	#传入页码，获取该页帖子的代码
	def getPage(self,pageNum):
		try:
			url = self.baseURL_left + str(pageNum) + self.baseURL_right
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			return unicode(response.read(), "gbk").encode("utf8")
			# return response.read().decode('gb2312')
		except urllib2.URLError, e:
			if hasattr(e,"reason"):
				print u"连接汽车之家，自驾游失败,错误原因",e.reason
				return None
	def gtitle(self):
		page = self.getPage(1)
		if not page:
			return None
		pattern = re.compile('<div class="maxtitle.*?>(.*?)</div>', re.S)
		result = re.search(pattern, page)
		if result:
			# print result.group(1)
			return result.group(1).strip()
		else:
			return None	
	def getContent(self):
		page = self.getPage(1)
		if not page:
			return None
		pattern = re.compile('<div class="conttxt" xname="content.*?>(.*?)<a href="#" name="shang"></a>(.*?)</div>', re.S)
		pattern1 = re.compile('<div class="x-reply font14" xname="content.*?>(.*?)<div class="last_editer_and_date">(.*?)</div>.*?</div>', re.S)
		items = re.findall(pattern,page)
		items1 = re.findall(pattern1, page)
		contents = []
		for item in items:
			contents.append(self.tool.replace(item[0]))
		for item in items1:
			contents.append(self.tool.replace(item[0]))	
		return contents	
	def start(self):
		title = self.gtitle()
		self.setFileTitle(title)
		try:
			contents = self.getContent()
			self.writeData(contents)
		except IOError,e:
			print "写入异常，原因" + e.message
		finally:
			print "写入任务完成"	
	def setFileTitle(self, title):
		if title is not None:
			self.file = open(title+".txt","w+")
		else:
			self.file = open(self.defaultTitle + ".txt", "w+")
	def writeData(self,contents):
		#向文件写入每一楼的信息
		for item in contents:
			# print item
			self.file.write(item)
def start():
	baseURL_left = 'http://club.autohome.com.cn/bbs/threadowner-c-200042-62195152-'
	baseURL_right = '.html#pvareaid=101435'
	bdtb = BDTB(baseURL_left, baseURL_right)
	return bdtb

def content():
	bdtb = start()
	return bdtb.getContent()

def title():
	bdtb = start()
	return bdtb.gtitle()	

