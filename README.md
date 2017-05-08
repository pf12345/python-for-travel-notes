# python-for-travel-notes
Python crawler crawling some websites(mafengwo、tripAdvisor)  travel notes and Save to mongodb database（使用python写的爬虫爬取一些旅游网站（如，蚂蜂窝、tripadvisor）中旅游游记，并将保持至mongodb数据库）

## Install

Use [python 2.7](https://www.python.org)、[mongodb](https://www.mongodb.com/download-center)、[PyMongo](http://api.mongodb.com/python/current/tutorial.html) and [Django-1.11](https://www.djangoproject.com/download/) in project

### Copy codes

```
$ git clone https://github.com/pf12345/python-for-travel-notes.git
```

### Config mongodb

Go to the code folder and enter:

```
$ cd ./tourism/settings.py

```
find line 83, modify "DBNAME" to your db name and Create a collection named "tourism" in db

### Run server
Go to the code folder and enter:

```
$ python manage.py runserver
```

Open your browser and visit http://127.0.0.1:8000

### Crawler article
for example: 

- ```mafengwo(蚂蜂窝)```:  <br>to save article [http://www.mafengwo.cn/i/5311724.html](http://www.mafengwo.cn/i/5311724.html),<br>
Open your browser and visit [http://127.0.0.1:8000/saveMafengwo/5311724](http://127.0.0.1:8000/saveMafengwo/5311724)

- ```tripAdvisor(猫途鹰)```: <br>to save article [https://www.tripadvisor.cn/TourismBlog-t5010.html?p=37085](https://www.tripadvisor.cn/TourismBlog-t5010.html?p=37085),<br>
Open your browser and visit [http://127.0.0.1:8000/saveTripAdvisor/5010](http://127.0.0.1:8000/saveTripAdvisor/5010)

### Urls

- 主页(游记列表): http://127.0.0.1:8000/
- 详情页: http://127.0.0.1:8000/detail/:id
- 保存马蜂窝游记：http://127.0.0.1:8000/saveMafengwo/:id
- 保存tripAdvisor(猫途鹰)游记：http://127.0.0.1:8000/saveTripAdvisor/:id


## LINKS

- [python中文基础教程](http://www.runoob.com/python/python-tutorial.html)
- [Django中文基础教程](http://www.runoob.com/django/django-first-app.html)
- [PyMongo 3.4.0 documentation](http://api.mongodb.com/python/current/tutorial.html)
- [beautifulsoup文档](http://beautifulsoup.readthedocs.io/zh_CN/latest/)
