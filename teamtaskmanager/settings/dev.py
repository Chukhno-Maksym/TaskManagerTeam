from teamtaskmanager.settings.base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h%@mc+5=mxy%8mfox(bt7h8_qtaa2cntdf^%4oxu8-obwx_r_z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}