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
from .utils import administrate_debug_message
import importlib
import sys, inspect

def applist():
    for app in settings.INSTALLED_APPS:
        if app in ['administrate.administrate', 'administrate']:
            continue


            #from "{}.administrate".format(app) import *
        try:
            module_name = '{}.administrate'.format(app)
            importlib.import_module(module_name)
            administrate_debug_message('{}.administrate OK'.format(app))
            clsmembers = inspect.getmembers(sys.modules[module_name], inspect.isclass)
            if len(clsmembers) > 0:
                # Делать типа обзор апликухи
                pass
            for c in clsmembers:
                print c[0].lower()
                c[1].get_urls()
        except:
            print sys.exc_info()
            administrate_debug_message('{}.administrate not found'.format(app))
            continue
        #print module


def get_urls():
    urlpatterns = [url(r'^$', index, name='index'), ]
    applist()
    return urlpatterns


urlpatterns = get_urls()
# url(r'^$', wrap(self.index), name='index'),
# url(r'^login/$', self.login, name='login'),
# url(r'^logout/$', wrap(self.logout), name='logout'),
