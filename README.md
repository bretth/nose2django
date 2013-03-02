Nose2-Django-Plugin
======================

A plugin for Nose2 that runs your django tests through the nose2 command and also supports [django-configurations](https://github.com/jezdez/django-configurations) settings management. It re-uses the django test runner and helper functions to initialize the test environment for django and setup the order of the test suite as per the django test runner, but lets Nose2 handle the test discovery and execution. 

Installation
--------------

For the moment install with pip directly from the repository. A package will be uploaded to pypi once I'm comfortable that it works as expected.

	$ pip install https://github.com/bretth/nose2django/zipball/master

Create a nose2.cfg file in your project's root directory (where manage.py is) and register the plugin:

	[unittest]
	plugins = nose2django.nose2django

	[django-runner]
	always-on = True

Usage
--------

Once installed the nose2 command will use the DJANGO_SETTINGS_MODULE environment variable and optionally DJANGO_CONFIGURATION (from django-configurations). They can both be passed in as options to the nose2 command. For example:

	nose2 --settings=example.settings.test --configuration=TestSettings


Acknowledgements
------------------

Nose2-Django-Plugin re-uses parts of the existing django test runner code as [licensed by django](https://raw.github.com/django/django/master/LICENSE). 








