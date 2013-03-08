

import unittest
import site
import os
from os.path import abspath, dirname, join
import sys

# just to test django is configured
from django.test import utils
from django.contrib.auth.models import User


site.addsitedir(join(dirname(abspath(__file__)),'djproject'))

class ATestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_dumb(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.assertIsNotNone(user.id)