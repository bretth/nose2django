nose2django
======================

A plugin pair for nose2 that runs your django (>=1.4) tests through the nose2 command and also supports [django-configurations](https://github.com/jezdez/django-configurations) settings management. It lets django initialise the test environment and setup the order of the test suite, but nose2/unittest2 handles the test discovery and execution.

*There is another project [django-nose2](https://github.com/jpellerin/django-nose2) authored by one of the nose2 devs which uses the standard django approach of setting an alternative test runner and running via manage.py. I prefer to not use manage.py to run my tests, and django these days makes it easier to move away from dependency on manage.py and django-admin.py as entry points.*

Installation
--------------

For the moment install with pip directly from the repository. A package will be uploaded to pypi once I'm comfortable that it works as expected.

	$ pip install https://github.com/bretth/nose2django/zipball/master

Create a nose2.cfg file in your project's root directory (where manage.py is) and register the plugins in the correct order:

	[unittest]
	plugins = nose2django.config
            nose2django.nose2django

    [django-config]
    always-on = True

    # optional settings
    settings = yourproject.settings
    configuration = YourTestConfiguration

	[django-runner]
	always-on = True


You can optionally set the `settings` and `configuration` to a django settings module and a django-configurations configuration. It takes precedence over any existing environment.

Usage
--------

As per nose2, optionally with either of the django-runner options.

	nose2 --settings=example.settings.test --configuration=TestSettings
	
Patterns
------------
For django app test driven development of apps you want only as much django settings as required. Create a tests folder in your top level directory (avoid using the name tests - use something like test_yourapp to avoid name clashes), and put a minimal settings file in there and an `__init__.py` file to make it importable. Something like:

	DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3' }
	}

	INSTALLED_APPS = (
    	'django.contrib.auth',
    	'django.contrib.contenttypes',
    	'django.contrib.sessions',
    	‘yourapp’,
	)
	ROOT_URLCONF=‘yourapp.urls', # if you have urls
	SECRET_KEY = '1234'

Acknowledgements
------------------

nose2django re-uses parts of the existing django test runner code as [licensed by django](https://raw.github.com/django/django/master/LICENSE).
