"""
Django settings for DjangoSandBox project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from unipath import Path

PROJECT_ROOT = Path(__file__).ancestor(3)
BASE_DIR = Path(__file__).ancestor(2)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# This should be stored as a system variable
SECRET_KEY = 'edjtf^(@ql2#z#e_=5&!78c6z%@zbx9#i+m$eu%9q9n9in-ks5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # http://django-debug-toolbar.readthedocs.org/
    'debug_toolbar',

    'helloworld',
    'modelsintroduction',
    'templatesintroduction',
    'home',
    'modelsadvanced',
    'viewsintroduction',
    'formsintroduction',
    'testintroduction',
    'authmodel',
    'errorsandlogging',
    'sessionsandcookies',
    'ajaxintroduction'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DjangoSandBox.urls'

WSGI_APPLICATION = 'DjangoSandBox.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS =  (
    os.path.join(PROJECT_ROOT, 'static'),
    os.path.join(PROJECT_ROOT, 'templatesintroduction', 'static'),
    os.path.join(PROJECT_ROOT, 'ajaxintroduction', 'static'),

)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

LOGIN_URL = '/auth/login/'
