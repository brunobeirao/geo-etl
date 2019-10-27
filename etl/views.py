# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .services import EtlService
from django.shortcuts import render


class GeoLocationProcessor():
    def __init__(self, filter_):
        self.filter = filter_
        self.etl_service = EtlService()

    def process(self):
        self.etl_service.run()
