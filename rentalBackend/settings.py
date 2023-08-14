"""
Django settings for rentalBackend project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# MPESA IMPORTS
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8j+=ff@&9#kfys28-d-t5tzu0epc-mdxao2)cl2ml9ogkh(!)7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'property',
    'unit',
    'tenant',
    'communication',
    'agreement',
    'landlord',
    'maintenanceRequest',
    'payment',
    'report',
    'corsheaders',
    'rest_framework',
    'psycopg2',
    'rest_framework.authtoken',
    'users',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django_daraja',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Added corsheaders middleware
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'rentalBackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rentalBackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#DATABASES = {
 #   'default': {
 #       'ENGINE': 'django.db.backends.sqlite3',
 #   }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rentalsdb',
        'USER': 'kupa',
        'PASSWORD': 'kupa@rent2023',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

## Frontend  interaction with API
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000'
]

# Adding JWT Cookie Authentication

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
}

SITE_ID = 1

#set REST_USE_JWT to be TRUE so that JWT authentication will be used by dj-rest-auth
REST_USE_JWT = True

#Defining the name of the cookie during authentication
JWT_AUTH_COOKIE = 'my-app-auth'

#AUTHENTICATION_BACKENDS will allow our users to be authenticated
#upon login and also allows us to login to the Django admin irrespective 
#of the django-allauth authentication backend

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Include email verification 
# specifying email should be used instead of username
# spsecified email must be provided by the user in order to register

ACCOUNT_AUTHENTICATION_METHOD = 'email'
#ACCOUNT_AUTHENTICATION_METHOD = 'password'
ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

#The ACCOUNT_CONFIRM_EMAIL_ON_GET is to allow the website to verify 
# the user when the user opens the link received in the email. 
# Then, we want the user to be redirected to the LOGIN_URL after verification, 
# so we specified our LOGIN_URL

#ACCOUNT_CONFIRM_EMAIL_ON_GET = True
LOGIN_URL = 'http://localhost:8000/users/login'

## THE MPESA ENVIRONMENT 
# Possible values: sandbox, production

MPESA_ENVIRONMENT = 'sandbox'

#Credentials for the daraja app


MPESA_CONSUMER_KEY = config('MPESA_CONSUMER_KEY')
MPESA_CONSUMER_SECRET = config('MPESA_CONSUMER_SECRET')
