import logging
import os
import unittest

from nose2.events import Plugin

log = logging.getLogger('nose2.plugins.djangorunner')

class DjangoRunner(Plugin):
    configSection = 'django-runner'
    commandLineSwitch = (None, 'django-runner', 
        'Initialises the django test environment and re-orders the test suite')

    logger = None
    djsettings = None
    djconfig = None

    def __init__(self):
        self.djsettings = self.config.as_str('settings')
        self.djconfig = self.config.as_str('configuration')
        self.addOption(self.set_settings, None,  'settings', 'DJANGO_SETTINGS_MODULE', 1)
        self.addOption(self.set_configuration, None,  'configuration', 'DJANGO_CONFIGURATION', 1)

    def set_settings(self, arg):
        """ Override config file settings with command lind option """
        self.djsettings = arg[0] 

    def set_configuration(self, arg):
        """ Override config file settings with command lind option """
        self.djconfig = arg[0]
    
    def handleArgs(self, event):
        """Nose2 hook for the handling the command line args"""
        self.verbosity = event.args.verbose

    def startTestRun(self, event):
        """Nose2 hook for the beginning of test running.
        Init the django environ and re-order the tests according to
        the django documented test runner behaviour.
        """

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
        # import here because django.test triggers a settings import
        from django.test.simple import reorder_suite, DjangoTestSuiteRunner
        from django.test.utils import setup_test_environment
        from django.conf import settings

        # Init the django default runner so we can call it's functions as needed
        self.dtsr = DjangoTestSuiteRunner()

        setup_test_environment()
        settings.DEBUG = False

        event.suite = reorder_suite(event.suite, (unittest.TestCase,))  
        
        self.old_config = self.dtsr.setup_databases()
        if self.verbosity > 0:
            # ensure that deprecation warnings are displayed during testing
            # the following state is assumed:
            # logging.capturewarnings is true
            # a "default" level warnings filter has been added for
            # DeprecationWarning. See django.conf.LazySettings._configure_logging
            self.logger = logging.getLogger('py.warnings')
            handler = logging.StreamHandler()
            logger.addHandler(handler)


    def afterTestRun(self, event):
        """Nose2 hook for the end of the test run"""
        from django.test.utils import teardown_test_environment
        if self.verbosity > 0:
            # remove the testing-specific handler
            self.logger.removeHandler(handler)
        self.dtsr.teardown_databases(self.old_config)
        teardown_test_environment()
