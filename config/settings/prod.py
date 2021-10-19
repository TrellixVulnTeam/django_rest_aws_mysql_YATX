from .base import *

ALLOWED_HOSTS = ['35.73.208.181']
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_rest_test_prd',
        'USER': 'dbmasteruser',
        'PASSWORD': '<27`OOCzI&cpUr>h8.!ltWMckEXRm~A|',
        'HOST': 'ls-5fd0ecff06f14a3a4426bc0fe64d2324e30566a6.clfiney1g8lc.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}