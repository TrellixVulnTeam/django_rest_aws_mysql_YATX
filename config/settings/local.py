from .base import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_rest_test',
        'USER': get_secret("LOCAL_DB_USER"),
        'PASSWORD': get_secret("LOCAL_DB_PWD"),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
