# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class OrgsConfig(AppConfig):
    name = 'orgs'

    def ready(self):
    	import orgs.signals
