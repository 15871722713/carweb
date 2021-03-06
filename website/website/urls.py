"""website URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from carweb import views as carweb_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$|^main/', carweb_views.index, name='home'),
    url(r'^about/', carweb_views.about, name='about'),
    url(r'^product/(?P<id>[0-9A-Z]+)$', carweb_views.product, name='product'),
    url(r'^news/', carweb_views.news, name='news'),
    url(r'^contact/', carweb_views.contact, name='contact'),
    url(r'^login/',carweb_views.login, name='login'),
    url(r'^data/',carweb_views.data, name='data'),
    url(r'^insert/',carweb_views.insert, name='insert'),
    url(r'^editdata/(?P<id>[0-9]+)$',carweb_views.editdata, name='editdata'),

]
