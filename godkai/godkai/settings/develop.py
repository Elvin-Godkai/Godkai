from .base import *  # NOQA


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'godkai',
        'USER': 'root',
        'PASSWORD': 'ykyk627627',
        'HOST': 'localhost',
        'PORT': 3306
    }
}