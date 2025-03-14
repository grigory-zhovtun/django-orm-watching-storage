import os
from environs import Env

env = Env()
env.read_env()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get("HOST_DB"),
        'PORT': os.environ.get("PORT_DB"),
        'NAME': os.environ.get("NAME_DB"),
        'USER': os.environ.get("USER_DB"),
        'PASSWORD': os.environ.get("PASSWORD_DB"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ.get("SITE_SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
