# Django settings for drunkduck project.
import os
import socket
PROJECT_DIR = os.getcwd()

DEBUG = True
TEMPLATE_DEBUG = DEBUG


hostname = socket.gethostname()


# format example:
# 'your local hostname': 'your package prefix ending with a dot character'
host_dir_map = {
    'Lawrence-Leachs-Mac-Pro.local': 'drunkduck.',      # Lawrence
    'mark-desktop': '',                                 # Mark
    'Administrators-iMac-3.local': 'quackcast.',        # Dan
    'ip-97-74-195-2.ip.secureserver.net': '',                                       # Mr. Server
}


db_map = {
    # Lawrence
    'Lawrence-Leachs-Mac-Pro.local': {
        'default': {
            'ENGINE': 'sqlite3',
            'NAME': 'dev.db',
        }
    },
    # Mark
    'mark-desktop': {
        'default': {
            'ENGINE': 'sqlite3',
            'NAME': 'mark_dev.db',
        }
    },
    # Dan
    'Administrators-iMac-3.local': {
        'default': {
            'ENGINE': 'sqlite3',
            'NAME': 'dev.db',
        }
    },
    # Server
    'ip-97-74-195-2.ip.secureserver.net': {
        'default': {
            'ENGINE': 'postgresql_psycopg2',
            'NAME': 'drunkduck_podcast',
            'USER': 'dd_podcast',
            'PASSWORD': 'G00dduck.10',
            'HOST': '',
            'PORT': '5432',
        }
    },
# Uncomment the lines below to add another definition map.
#    '<YOUR_LOCAL_HOST_NAME>': {
#        'default': {
#            'ENGINE': '',      # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3', or 'oracle'.
#            'NAME': '',        # Or path to database file if using sqlite3
#            'USER': '',        # Not used with sqlite3
#            'PASSWORD': '',    # Not used with sqlite3
#            'HOST': '',        # Set to empty string for localhost. Not used with sqlite3.
#            'PORT': ''         # Set to empty string for default. Not used with sqlite3.
#        }
#    },
}


ADMINS = (
    ('Lawrence Leach', 'lleach@wowio.com'),
)

MANAGERS = ADMINS


DATABASES = db_map[hostname]


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')
STATIC_DOC_ROOT = MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(myzf(s$x^f03p6xl6y^quk9ot$#nysimjvo=nzd69ccgl^kub'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = host_dir_map[hostname] + 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.media"
)

TAGGING_AUTOCOMPLETE_JS_BASE_URL = '/media/js'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'pagination',
    'tagging',
    'tagging_autocomplete',    
    host_dir_map[hostname] + 'podcast'
)
