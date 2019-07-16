"""
Django settings for aurora project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

from aurora import config as CF

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=*+t-qchu_$#hhf9m-n45s7p=@n46(zmf^mof$+cdaa0t6h8pq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = CF.DEBUG

ALLOWED_HOSTS = CF.ALLOWED_HOSTS

BASE_URL = CF.BASE_URL

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cron',
    'rest_framework',
    'drf_yasg',
    'bag_transfer',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'bag_transfer.middleware.AuthenticationMiddlewareJWT',
]

ROOT_URLCONF = 'aurora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'bag_transfer', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bag_transfer.context_processors.gtm_id',
            ],
        },
    },
]

LOGIN_REDIRECT_URL = 'app_home'

WSGI_APPLICATION = 'aurora.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': CF.DEFAULT_DB,
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'bag_transfer.User'
LOGIN_REDIRECT_URL = '/app'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = CF.TIME_ZONE
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = CF.STATIC_ROOT
STORAGE_ROOT_DIR = CF.STORAGE_ROOT_DIR
DELIVERY_QUEUE_DIR = CF.DELIVERY_QUEUE_DIR


# Transfer settings
TRANSFER_FILESIZE_MAX = CF.TRANSFER_FILESIZE_MAX
TRANSFER_UPLOADS_ROOT = CF.TRANSFER_UPLOADS_ROOT
TRANSFER_EXTRACT_TMP = CF.TRANSFER_EXTRACT_TMP
UPLOAD_LOG_FILE = CF.UPLOAD_LOG_FILE


# Django Cron
CRON_CLASSES = [
    "bag_transfer.lib.cron.DiscoverTransfers",
    "bag_transfer.lib.cron.DeliverTransfers",
    "django_cron.backends.lock.file.FileLock",
]

#Django Cron Lock
DJANGO_CRON_LOCK_BACKEND="django_cron.backends.lock.file.FileLock"

# Email
EMAIL_HOST = CF.EMAIL_HOST
EMAIL_PORT = CF.EMAIL_PORT
EMAIL_HOST_USER = CF.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = CF.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = CF.EMAIL_USE_TLS
EMAIL_USE_SSL = CF.EMAIL_USE_SSL
EMAIL_OVERRIDE = CF.EMAIL_OVERRIDE
EMAIL_OVERRIDE_USERS = CF.EMAIL_OVERRIDE_USERS
DEFAULT_FROM_EMAIL = CF.DEFAULT_FROM_EMAIL
SERVER_EMAIL = CF.SERVER_EMAIL

# Unit Test configs
TEST_BAGS_DIR = CF.TEST_BAGS_DIR
TEST_USER = CF.TEST_USER


# Post-accession callbacks
DELIVERY_URL = getattr(CF, 'DELIVERY_URL', None)
API_KEY = getattr(CF, 'API_KEY', None)

# ArchivesSpace configs
ASPACE = CF.ASPACE

# Google Analytics configs
GTM_ID = CF.GTM_ID
