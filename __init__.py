# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'sb'
VERSION = (0, 0, 1)

__all__=['base',]

def get_version(svn=False):
    "Returns the version as a human-format string."
    return '.'.join([str(i) for i in VERSION])