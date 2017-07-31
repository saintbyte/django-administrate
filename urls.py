# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from administrate import administrate
from .views import LoginView
import traceback
from django.apps import apps

__author__ = 'sb'
from django.conf.urls import url
from .views import index
from .utils import administrate_debug_message
import importlib
import sys, inspect
print ('urls.py')
urlpatterns = administrate.get_urls() # If you want use include

