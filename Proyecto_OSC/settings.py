"""
Django settings for Proyecto_OSC project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c6)7gtsd*486fqnof&$2f=43*44z^k4l66nfndf_z#^bg&p4)y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'crispy_forms',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Proyecto_OSC.urls'

WSGI_APPLICATION = 'Proyecto_OSC.wsgi.application'


# DATABASES = {
#     'default': {
#        'NAME': 'Proyecto_OSC',
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'USER': 'postgres',
#        'PASSWORD': 'aa121292',
#        'HOST': '',
#
#        'PORT': '5432'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es_mx'
TIME_ZONE = 'UTC'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(CURRENT_PATH, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = 'static/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
                    os.path.join(CURRENT_PATH, 'static'),
)