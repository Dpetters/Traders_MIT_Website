import os
ROOT = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ("""name, email"""),
)
MANAGERS = ADMINS

DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': ROOT + '/database.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
