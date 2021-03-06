
# import django_heroku
"""
Django settings for pricetracker project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import dotenv# we have dowloaded python-dotenv package from pip
import os
import sys


dotenv.load_dotenv()# we have dowloaded python-dotenv package from pip ,
                    #this loads all variables from .env to os,and we retrive this from
                    #os.getenv() method



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print('$'*20)
#print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')#os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG=bool(os.environ.get('DEBUG', ''))
DEBUG=True
print(f'debug is {DEBUG*5}')#heroku-django-uploaded image is not displayed if DEBUG=False

#if you set DEBUG=True or False in heroku config then bool(os.environ.get('DEBUG', '')) will be True
#bcoz os.environ.get('DEBUG')give sting value ,'True'or 'False'...DEBUG should be boolean value
#bool('True')==bool('false') gives True.....bool('') gives False
#otherwise if not set than bool(os.environ.get('DEBUG', '')) will be False coz bool('') is false.
#and if it is false heroku-django-uploaded image will not be displayed in website in production



ALLOWED_HOSTS = ['trackass-heroku.herokuapp.com','127.0.0.1']




# Application definition

INSTALLED_APPS = [
    "scrapyproject",
    'users.apps.UsersConfig',
    'track.apps.TrackConfig',
    'background.apps.BackgroundConfig',
    'crispy_forms',

    'background_task',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'storages', #storages and boto3 are used for interacting to AWS
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    
]

ROOT_URLCONF = 'pricetracker.urls'

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

WSGI_APPLICATION = 'pricetracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')#for heroku deployment

STATIC_URL = '/static/'
CRISPY_TEMPLATE_PACK='bootstrap4'
LOGIN_REDIRECT_URL='track-home'
LOGIN_URL='login'

MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'

STATICFILES_DIRS=(
    
    os.path.join(BASE_DIR,'mystaticfiles'),
)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER =os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE=False
AWS_DEFAULT_ACL=None

#whatever the imagefield is there in database or models.py, those will be come from aws s3 bucket ,not img_url field ,this will
#come from local file.


#note that heroku supports statis files....i mean if there is any static file or media file,
#then heroku supports that files ,only if user want to uplaod new images or files or pdf then it is 
#not possible in heroku
#if you are showing images or pdf from alraedy uploaded manually media files into heroku then yes it will show
#those media pdf and images,,,,only new uploadation not allowed.
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
S3_USE_SIGV4 = True
AWS_S3_REGION_NAME=os.getenv('AWS_S3_REGION_NAME')



# django_heroku.settings(locals())