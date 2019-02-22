# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Car(models.Model):
	"""docstring for Car"""
	name = models.CharField(max_length=30)
	img = models.ImageField(upload_to="img")
	img1 = models.ImageField(upload_to="img")
	img2 = models.ImageField(upload_to="img")
	img3 = models.ImageField(upload_to="img")
	img4 = models.ImageField(upload_to="img")
	img5 = models.ImageField(upload_to="img")
	introduction = models.CharField(max_length=50)
	introductiondetail = models.CharField(max_length=500)
	producttype = models.CharField(max_length=2)

	cartype = models.CharField(max_length=30)
	price = models.CharField(max_length=30)

	b1 = models.CharField(max_length=30)
	b2 = models.CharField(max_length=30)
	b3 = models.CharField(max_length=30)
	b4 = models.CharField(max_length=30)
	b5 = models.CharField(max_length=30)
	b6 = models.CharField(max_length=30)
	b7 = models.CharField(max_length=30)
	b8 = models.CharField(max_length=30)
	b9 = models.CharField(max_length=30)
	b10 = models.CharField(max_length=30)
	b11 = models.CharField(max_length=30)
	b12 = models.CharField(max_length=30)
	b13 = models.CharField(max_length=30)
	b14 = models.CharField(max_length=30)
	b15 = models.CharField(max_length=30)
	b16 = models.CharField(max_length=30)
	b17 = models.CharField(max_length=30)
	b18 = models.CharField(max_length=30)
	b19 = models.CharField(max_length=200)
	b20 = models.CharField(max_length=400)

	



	def __unicode__(self):
		return self.name