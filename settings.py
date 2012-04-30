import os
ROOT = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

MEDIA_MODELS = {}

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

PROD_MEDIA_ROOT = ROOT + '/prod_media/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ROOT + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ROOT + '/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'compressor.finders.CompressorFinder'
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'u^z=+ez-97)*9(4d1%$++&3n^+h9f#x_*g!4h9=#^^^9_k5w5+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
	ROOT + "/templates",
)

# Email Settings
AWS_ACCESS_KEY_ID = 'AKIAJD32PEOKIG4RK3NQ'
AWS_SECRET_ACCESS_KEY = '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'
EMAIL_BACKEND = 'django_ses.SESBackend'

# Emails sent to users will be coming from this email address
DEFAULT_FROM_EMAIL = 'Traders@MIT <traders@mit.edu>'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'compressor',
    'core',
    'event',
    'south'
)

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [      'Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Underline',
              '-', 'Link', 'Unlink',
              '-', 'Maximize',
            ],
            [      'HorizontalRule',
              '-', 'BulletedList', 'NumberedList',
            ]
        ],
        'width': 586,
        'resize_maxWidth' : 586,
        'resize_minWidth' : 586,
        'resize_minHeight' : 300,
        'height': 210,
        'skin':'kama',
        'toolbarCanCollapse': False,
        'forcepasteasplaintext': True,
        'removePlugins':'elementspath'
    },
}

CKEDITOR_MEDIA_PREFIX = "/static/lib/ckeditor/"

CKEDITOR_UPLOAD_PATH = "%sckeditor" % MEDIA_ROOT

CKEDITOR_PATH = "ckeditor/"

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'standard': {
			'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		}
	},
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
		'file_handler': {
			'level':'DEBUG',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': ROOT + '/logs/traders.log',
			'maxBytes': 1024*1024*10,
			'backupCount': 5,
			'formatter':'standard',
		},
    },
    'loggers': {
        'django.request': {
            'handlers': ['file_handler'],
            'level': 'WARNING',
        },
    }
}

try:
    from settings_local import *
except ImportError:
    from settings_prod import *
