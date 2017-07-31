# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
__author__ = 'sb'

from django.conf.urls import url

class Administrate(object):
    def __init__(self):
        print ("Administrate __init__")
        self._registry = {}

    def register(self,*args,**kwargs):
        pass
         #self._registry.append(args[0])

    def applist(self):
        pass

    def index(self):
        print 'index'
        return HttpResponse('OK')

    def get_urls(self,request, *callback_args, **callback_kwargs):
        print 'administrate get_urls'
        self.applist()
        urlpatterns = [
            url(r'^$', self.index, name='administrate_index'),
        ]
        return urlpatterns

class BaseAdministrateView(object):
    pass