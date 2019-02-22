# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from urlparse import unquote
from django.contrib import auth
from . import models

# Create your views here.

def index(request):
	return render(request,'main.html')

def about(request):
	return render(request,'about.html')

def product(request,id):
	if str(id) == "ALL":
		cars = models.Car.objects.all()
		return render(request,'product.html',{"cars":cars})
	if str(id) == "A":
		cars = models.Car.objects.filter(producttype=id)
		return render(request,'product.html',{"cars":cars})
	if str(id) == "B":
		cars = models.Car.objects.filter(producttype=id)
		return render(request,'product.html',{"cars":cars})
	if str(id) == "C":
		cars = models.Car.objects.filter(producttype=id)
		return render(request,'product.html',{"cars":cars})
	if str(id) == "D":
		cars = models.Car.objects.filter(producttype=id)
		return render(request,'product.html',{"cars":cars})
	cars = models.Car.objects.get(id=id)
	return render(request,'product_detail.html',{"cars":cars})

def news(request):
	return render(request,'news.html')

def contact(request):
	return render(request,'contact.html')

def login(request):
	if(request.method == 'POST'):
		username = request.POST.get("username",None)
		password = request.POST.get("password",None)
		print 'username:',username
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			request.session['user'] = username # 将session信息记录到浏览器
			request.session['psw'] = password
			# Correct password, and the user is marked "active"
			auth.login(request, user)
			return HttpResponseRedirect('/data/')
		else:
			return render(request, 'login.html', {'error_msg': '用户名或密码输入错误!'})

def data(request):
	datas = {}
	if(request.method == 'POST'):
		print request.FILES["file"]
		body = request.body
		for x in body.split('&'):
			if x.split('=')[0] != 'csrfmiddlewaretoken':
				datas[x.split('=')[0]] = unquote(x.split('=')[1].encode('gb18030')).decode('utf-8')
		if datas.has_key('csrfmiddlewaretoken'):
			datas.pop('csrfmiddlewaretoken')
		models.Car.objects.create(**datas)
	cars = models.Car.objects.all()
	return render(request,'data.html',{"cars":cars})

def editdata(request,id):
	cars = models.Car.objects.get(id=id)
	return render(request,'product_edit.html',{"cars":cars})

def insert(request):
	return render(request,'product_edit01.html')