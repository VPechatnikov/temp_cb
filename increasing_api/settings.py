"""
Django settings for increasing_api project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j!o&%id-2rtr6%&#hds1nb&sue4id*q(7hqt3*spc-cf2$t)fn'

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
    'increasing'
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

ROOT_URLCONF = 'increasing_api.urls'

WSGI_APPLICATION = 'increasing_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'increasing_api.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s:%(name)s:%(levelname)s:%(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(asctime)s:%(name)s:%(levelname)s - %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'logfile': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.environ.get('API_LOG_FILE','/var/log/django/increasing_api.log'),
            'maxBytes': 100000,
            'backupCount': 2,
            'formatter': 'simple',
        },
        'warnlogfile': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.environ.get('API_LOG_FILE','/var/log/django/warn_increasing_api.log'),
            'maxBytes': 100000,
            'backupCount': 2,
            'formatter': 'simple',
        },
        'debuglogfile': {
            'level':'DEBUG',
            'filters': ['require_debug_true'],
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.environ.get('API_LOG_FILE','/var/log/django/debug_increasing_api.log'),
            'maxBytes': 100000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'console':{
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'increasing': {
            'handlers': ['console', 'logfile', 'debuglogfile'],
            'level':'DEBUG',
            'propagate': True
        },
        'stats_updater': {
            'handlers': ['console', 'logfile', 'debuglogfile'],
            'level':'DEBUG',
            'propagate': True
        },
        'django': {
            'handlers': ['console', 'warnlogfile'],
            'level':'WARNING'
        },
        'django.request': {
            'handlers': ['logfile', 'warnlogfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        'py.warnings': {
            'handlers': ['console'],
            'level':'WARNING'
        }
    }
}
