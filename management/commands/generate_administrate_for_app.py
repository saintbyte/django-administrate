# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'sb'

from django.core.management.base import BaseCommand, CommandError
import sys, os, time
from django.utils.translation import ugettext as _

class Command(BaseCommand):
   help = 'Generate administrate file for appication'

   def handle(self, *args, **options):
       sys.stdout.write(_('Start'))
       sys.stdout.write(_('Finish'))