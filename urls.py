# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from .views import LoginView

from django.apps import apps

__author__ = 'sb'
from django.conf.urls import url
from .views import index

def applist():
    for app in settings.INSTALLED_APPS:
        print app


def get_urls():
    applist()
    urlpatterns = [url(r'^$', wrap(self.index), name='index'),]

urlpatterns = get_urls()
            #url(r'^$', wrap(self.index), name='index'),
            #url(r'^login/$', self.login, name='login'),
            #url(r'^logout/$', wrap(self.logout), name='logout'),
