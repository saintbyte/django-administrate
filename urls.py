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


def applist():
    for app in settings.INSTALLED_APPS:
        if app in ['administrate.administrate', 'administrate']:
            continue
        try:
            importlib.import_module('{}.administrate'.format(app))
            administrate_debug_message('{}.administrate OK'.format(app))
        except:
            administrate_debug_message('{}.administrate not found'.format(app))


def get_urls():
    urlpatterns = [url(r'^$', index, name='index'), ]
    applist()
    return urlpatterns


urlpatterns = get_urls()
# url(r'^$', wrap(self.index), name='index'),
# url(r'^login/$', self.login, name='login'),
# url(r'^logout/$', wrap(self.logout), name='logout'),
