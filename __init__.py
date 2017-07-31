# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from base import Administrate
administrate = Administrate()

__author__ = 'sb'
VERSION = (0, 0, 1)


__all__=['base','urls','administrate']


print administrate

def register(*args,**kwargs):
    print 'register'
    print args
    administrate.register(*args,**kwargs)

def urls(request, *callback_args, **callback_kwargs):
    print('urls')
    return administrate.get_urls(request, *callback_args, **callback_kwargs)

def get_version(svn=False):
    "Returns the version as a human-format string."
    return '.'.join([str(i) for i in VERSION])