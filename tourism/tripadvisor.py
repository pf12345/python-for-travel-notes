# -*- coding:utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import re



class TRIPADVISOR:
	#初始化，传入基地址，是否只看楼主的参数
	def __init__(self,article_id):
		self.baseArticleId = article_id
		self.baseURL = 'https://www.tripadvisor.cn/TourismBlog-t' + article_id + '.html'
		self.defaultTitle = '美丽游'
		self.oldIds = []

	
	def getPage(self):
		try:
			url = self.baseURL
			headers = { 
				'Cookie' : 'TAUnique=%1%enc%3A16fIcz1IL9r3d0Se3vnlWwSXBnFUUjJkPRsB9ycMVWUVAETMq8nxvA%3D%3D; TASSK=enc%3AACT7KYOKiWRj6fNmPUSXdeiIo6GiEykqEMtbuSiYxm%2FRiu86U4i27pZpD%2Fh9FEYpT1Cnw4sIlSyiHui2au3F8qUh5VAwW3IzIawio%2FlRxdjZFDS%2FZ6xvchfNmGbeIYLo3g%3D%3D; __gads=ID=695e2d96a51eacf5:T=1492823236:S=ALNI_MYQAZWbALXmsGADsd8lyDfYcEtbZA; TAAuth2=%1%3%3Abca7967c9508baa410ca3bacdda65622%3AANQo8zXguDhxlyYpV6FFu5sEYths72817lzt4OdtQjbqTc%2BbyYlX3gbKRGradPA8IFOr9muTGDS0S6IuVcBx4rTUKb8VU2po7XynpGtZKEhsrWQyBJ%2FILcDLvfYctgbO%2Ffgs56M9plnqDPel%2BQpE%2Fq1UfP7i8y3xMUm4izKeNPKLdnkE%2Bcrjck3D%2BXUhme3SEA%3D%3D; ServerPool=R; CM=%1%HanaPersist%2C%2C-1%7CHanaSession%2C%2C-1%7CFtrSess%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C2%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Csesssticker%2C%2C-1%7CViatorMCSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; VRMCID=%1%V1*id.16631*llp.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*e.1494165793923; _jzqy=1.1493561126.1493561126.1.jzqsr=baidu|jzqct=tripadvisor.-; _jzqckmp=1; _smt_uid=58faad31.29381f99; CommercePopunder=SuppressAll*1493561203126; TAReturnTo=%1%%2FTourismBlog-t5589.html; roybatty=TNI1625!AGJjEEvtS6Pq9BBbDEnO6Q%2F1Y3hmL8hWIubITauHWFPCQcWNEr%2BuZsu9F%2BCxSLZuqYbnzDAQHDEPUS9F0jRZeR%2Fdaf0AyWa4At350%2BaTecUVAWUo4YdGqTlRZvfoAXoLICakG%2FspUGfcKKdSXiz4GfmcIfxB33SeF5%2BowbgZJ2a1%2C1; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.293920_111l319081_111l1834249_111l303770_111*DSM.1493563121681*RS.1; TASession=%1%V2ID.FC91BEC954F5FCDA27735DC631C502D4*SQ.81*MC.16631*LR.http%3A%2F%2Fbzclk%5C.baidu%5C.com%2Fadrc%5C.php%3Ftpl%3Dtpl_10085_14394_1%26l%3D1051856896%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3Dtripadvisor%26oq%3Dtrs%26rqlang%3Dcn%26inputT%3D601737%26bs%3Dtrs*LP.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*LS.TripFullCardAjax*GR.4*TCPAR.31*TBR.57*EXEX.86*ABTR.67*PHTB.38*FS.63*CPU.38*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.0A163614820ADDDDDE9B86436F815AC5*FA.1*DF.0*TRA.true*LD.293910; TAUD=LA-1493560993858-1*RDD-1-2017_04_30*LG-2129066-2.1.F.*LD-2129067-.....; _ga=GA1.2.350032807.1492823342; _gat_UA-79743238-4=1; ki_t=1492823618927%3B1493561127388%3B1493563253494%3B2%3B20; ki_r=; _jzqa=1.4359405283164852000.1492823345.1492823345.1493561126.2; _jzqc=1; _qzja=1.672263528.1492823344932.1492823344933.1493561135745.1493562986315.1493563253563..0.0.25.2; _qzjb=1.1493561135745.13.0.0.0; _qzjc=1; _qzjto=13.1.0; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1492823345,1493561126; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1493563254; _jzqb=1.13.10.1493561126.1',
				'Host': 'www.tripadvisor.cn',
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
			}
			request = urllib2.Request(url, {}, headers)
			response = urllib2.urlopen(request)
			soup = BeautifulSoup(response.read().decode('utf8').encode('utf8'), "html.parser")
			return soup
		except Exception, e:
			if hasattr(e,"reason"):
				print u"连接失败,错误原因",e.reason
				return None

	def getTitle(self):
		soup = self.getPage()
		if soup:
			return soup.select('.title-text')[0].string
		else:
			return ''	

	def getArticleCards(self):
		soup = self.getPage()
		cards = []
		if soup:
			cardNodes = soup.select('.strategy-content')
			for node in cardNodes:
				cards.append(node['card-id'])
		return cards		

	def getOneContent(self, id):
		url = 'https://www.tripadvisor.cn/TripFullCardAjax-t'+self.baseArticleId+'?card='+ str(id)
		try:
			headers = { 
				'Cookie' : 'TAUnique=%1%enc%3A16fIcz1IL9r3d0Se3vnlWwSXBnFUUjJkPRsB9ycMVWUVAETMq8nxvA%3D%3D; TASSK=enc%3AACT7KYOKiWRj6fNmPUSXdeiIo6GiEykqEMtbuSiYxm%2FRiu86U4i27pZpD%2Fh9FEYpT1Cnw4sIlSyiHui2au3F8qUh5VAwW3IzIawio%2FlRxdjZFDS%2FZ6xvchfNmGbeIYLo3g%3D%3D; __gads=ID=695e2d96a51eacf5:T=1492823236:S=ALNI_MYQAZWbALXmsGADsd8lyDfYcEtbZA; TAAuth2=%1%3%3Abca7967c9508baa410ca3bacdda65622%3AANQo8zXguDhxlyYpV6FFu5sEYths72817lzt4OdtQjbqTc%2BbyYlX3gbKRGradPA8IFOr9muTGDS0S6IuVcBx4rTUKb8VU2po7XynpGtZKEhsrWQyBJ%2FILcDLvfYctgbO%2Ffgs56M9plnqDPel%2BQpE%2Fq1UfP7i8y3xMUm4izKeNPKLdnkE%2Bcrjck3D%2BXUhme3SEA%3D%3D; ServerPool=R; CM=%1%HanaPersist%2C%2C-1%7CHanaSession%2C%2C-1%7CFtrSess%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C2%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Csesssticker%2C%2C-1%7CViatorMCSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; VRMCID=%1%V1*id.16631*llp.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*e.1494165793923; _jzqy=1.1493561126.1493561126.1.jzqsr=baidu|jzqct=tripadvisor.-; _jzqckmp=1; _smt_uid=58faad31.29381f99; CommercePopunder=SuppressAll*1493561203126; TAReturnTo=%1%%2FTourismBlog-t5589.html; roybatty=TNI1625!AGJjEEvtS6Pq9BBbDEnO6Q%2F1Y3hmL8hWIubITauHWFPCQcWNEr%2BuZsu9F%2BCxSLZuqYbnzDAQHDEPUS9F0jRZeR%2Fdaf0AyWa4At350%2BaTecUVAWUo4YdGqTlRZvfoAXoLICakG%2FspUGfcKKdSXiz4GfmcIfxB33SeF5%2BowbgZJ2a1%2C1; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.293920_111l319081_111l1834249_111l303770_111*DSM.1493563121681*RS.1; TASession=%1%V2ID.FC91BEC954F5FCDA27735DC631C502D4*SQ.81*MC.16631*LR.http%3A%2F%2Fbzclk%5C.baidu%5C.com%2Fadrc%5C.php%3Ftpl%3Dtpl_10085_14394_1%26l%3D1051856896%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3Dtripadvisor%26oq%3Dtrs%26rqlang%3Dcn%26inputT%3D601737%26bs%3Dtrs*LP.%2F-a_ttcampaign%5C.MTYpc-a_ttgroup%5C.title-m16631*LS.TripFullCardAjax*GR.4*TCPAR.31*TBR.57*EXEX.86*ABTR.67*PHTB.38*FS.63*CPU.38*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.0A163614820ADDDDDE9B86436F815AC5*FA.1*DF.0*TRA.true*LD.293910; TAUD=LA-1493560993858-1*RDD-1-2017_04_30*LG-2129066-2.1.F.*LD-2129067-.....; _ga=GA1.2.350032807.1492823342; _gat_UA-79743238-4=1; ki_t=1492823618927%3B1493561127388%3B1493563253494%3B2%3B20; ki_r=; _jzqa=1.4359405283164852000.1492823345.1492823345.1493561126.2; _jzqc=1; _qzja=1.672263528.1492823344932.1492823344933.1493561135745.1493562986315.1493563253563..0.0.25.2; _qzjb=1.1493561135745.13.0.0.0; _qzjc=1; _qzjto=13.1.0; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1492823345,1493561126; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1493563254; _jzqb=1.13.10.1493561126.1',
				'Host': 'www.tripadvisor.cn',
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
			}
			request = urllib2.Request(url, {}, headers)
			response = urllib2.urlopen(request)
			soup = BeautifulSoup(response.read().decode('utf8').encode('utf8'))
			return soup
		except Exception, e:
			if hasattr(e,"reason"):
				print u"连接失败,错误原因",e.reason
				return None		 

	def getContent(self):
		cards = self.getArticleCards()
		html = ''
		text = ''
		firstImg = ''
		for card in cards:
			html += self.getOneContent(card).prettify()
			for string in self.getOneContent(card).stripped_strings:
				text += string.replace('function(.*?)\\(\\)', '')
		
		pattern = re.compile('http(.*?)(jpg|png)')


		if re.search(pattern, text):
			firstImg = re.search(pattern, text).group(0)

		return {"html": html, "text": text, "firstImg": firstImg}

	def getUser(self):
		try:
			soup = self.getPage()

			if not soup:
				return {"name": '', "avatar": '', "oldCreated": ''}

			name = soup.select('.strategy-info a')[0].string

			avatar = soup.select('.blog-head-image')[0]['src']

			_time = ''

			return {"name": name, "avatar": avatar, "oldCreated": _time}

		except Exception, e:
			if hasattr(e,"reason"):
				print u"连接失败,错误原因",e.reason
				return None


	def getWebsite(self):
		return {"url": self.baseURL, "name": "tripAdvisor"}
	

def getTripAdvisor(id):
	return TRIPADVISOR(id)

# tripadvisor = TRIPADVISOR('5578')

# tripadvisor.getArticleCards()

# tripadvisor.getContent()

# print tripadvisor.getUser()

# tripadvisor.getTitle()

