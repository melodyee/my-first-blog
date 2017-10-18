# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.
from django.utils import timezone


# models.Model means Post is a Django Model
# 一个对象 对应数据库中的 一个表 blog_Post
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
