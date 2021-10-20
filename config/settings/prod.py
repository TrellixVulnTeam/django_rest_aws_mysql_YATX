from .base import *

ALLOWED_HOSTS = ['35.73.208.181']
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_rest_test_prd',
        'USER': get_secret("PRD_DB_USR"),
        'PASSWORD': get_secret("PRD_DB_PWD"),
        'HOST': get_secret("PRD_DB_HOST"),
        'PORT': '3306',
    }
}