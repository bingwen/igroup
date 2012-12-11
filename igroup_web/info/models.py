# coding: utf-8

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

# ===================================
class org(models.Model):
	"""info for org"""
	name = models.CharField(max_length=50, verbose_name=u"Org名")
	des = models.CharField(blank=True, max_length=100, verbose_name=u"简介")
	password = models.CharField(max_length=30, verbose_name=u"暗号")

	def __unicode__(self):
		return self.name

class group(models.Model):
	"""info for group"""
	name = models.CharField(max_length=50, verbose_name=u"Group名")
	des = models.CharField(blank=True, max_length=100, verbose_name=u"简介")
	org = models.ForeignKey(org, verbose_name=u"所属Org")

	def __unicode__(self):
		return self.name

class person(models.Model):
	"""info model for person"""
	name = models.CharField(max_length=30, verbose_name=u"名字")
	title = models.CharField(max_length=30, verbose_name=u"Title")
	phone_number = models.CharField(max_length=30, verbose_name=u"电话号码")
	qq = models.PositiveIntegerField(blank=True, null=True, verbose_name=u"QQ")
	mail = models.EmailField(blank=True, max_length=75, verbose_name=u"邮箱")
	weibo = models.URLField(blank=True, max_length=50, verbose_name=u"微博")
	birthday = models.DateField(blank=True, verbose_name=u"生日")
	group = models.ManyToManyField(group, blank=True, verbose_name=u"所属Group")

	def __unicode__(self):
		return self.name






