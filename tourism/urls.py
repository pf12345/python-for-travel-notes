"""tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
import settings

from . import view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.list),
    url(r'^saveMafengwo/(.*?)$', view.saveMafengwo),
    url(r'^saveTripAdvisor/(.*?)$', view.saveTripAdvisor),
    url(r'^saveCtrip/', view.saveCtrip),
    url(r'^detail/(.*?)$', view.detail),
    url(r'^list/', view.list),
    url(r'^getList/', view.getList),
    url(r'^getAddressList/', view.getAddressList)
]

media_root = os.path.join(settings.BASE_DIR,'static')
urlpatterns += static('/', document_root=media_root)
