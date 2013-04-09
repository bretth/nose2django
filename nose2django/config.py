import logging
import os
import unittest

from nose2.events import Plugin

log = logging.getLogger('nose2.plugins.djangorunner')

class DjangoConfig(Plugin):
    configSection = 'django-config'
    commandLineSwitch = (None, 'django-config',
        'Initialises the django test environment and re-orders the test suite')

    logger = None
    djsettings = None
    djconfig = None

    def __init__(self):
        self.djsettings = self.config.as_str('settings')
        self.djconfig = self.config.as_str('configuration')
        self.addOption(self.set_settings, None,  'settings', 'DJANGO_SETTINGS_MODULE', 1)
        self.addOption(self.set_configuration, None,  'configuration', 'DJANGO_CONFIGURATION', 1)

    def handleArgs(self, event):
        """Nose2 hook for the handling the command line args"""
        # settings resolution order:
        # command line > cfg file > environ
        if self.djsettings:
            os.environ['DJANGO_SETTINGS_MODULE'] = self.djsettings
        if self.djconfig:
            os.environ['DJANGO_CONFIGURATION'] = self.djconfig
        # test for django-configurations package
        try:
            from configurations import importer
            importer.install()
        except ImportError:
            pass
        from django.conf import settings

        try:
            from south.management.commands import patch_for_test_db_setup
            patch_for_test_db_setup()
        except ImportError:
            pass


    def set_settings(self, arg):
        """ Override config file settings with command lind option """
        self.djsettings = arg[0]

    def set_configuration(self, arg):
        """ Override config file settings with command lind option """
        self.djconfig = arg[0]




