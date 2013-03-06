

import unittest
import site
import os
from os.path import abspath, dirname, join
import sys

# This currently just allows us to run nose2 against a test django project with the django-runner plugin enabled
# in nose2.cfg to prove that it will setup the django environment without error and run the test.

site.addsitedir(join(dirname(abspath(__file__)),'djproject'))

class ATestCase(unittest.TestCase):
	def setUp(self):
		pass

	def test_dumb(self):
		self.assertEqual(1+1, 2)