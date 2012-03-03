import os
ROOT = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	("Traders Exec", "traders-exec@mit.edu"),
)
MANAGERS = ADMINS

STATICFILES_DIRS = (
    ROOT + "/static/",
)

DATABASES = {
	'default':{
		'ENGINE':'django.db.backends.mysql',
		'NAME':'traders_main',
		'USER':"traders",
		'PASSWORD':"pov68dey",
		'HOST':"sql.mit.edu",
		'PORT':"3306",
	}
}
