from .base import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_rest_test',
        'USER': 'root',
        'PASSWORD': 'root1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
