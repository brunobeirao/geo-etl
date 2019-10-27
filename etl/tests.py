# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .services import EtlService
from django.conf import settings
from django.test import TestCase

service = EtlService()
settings.configure()


class TestRequests(TestCase):

    def test_post(self):
        service.run()
