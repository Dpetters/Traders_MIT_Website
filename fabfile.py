import os

from fabric.api import local, settings as fabric_settings
from fabric.contrib import django as fabric_django

fabric_django.settings_module('settings')

__all__= ["commit_data", "load_data"]

DATA_MODELS = {
    'core': ['course', 'graduationyear', 'boardmember', 'execmember']
}
LOCAL_DATA_MODELS = {}

def load_data():
    local("python copy_media.py in")
    local("python manage.py loaddata ./initial_data.json")
                
def commit_data():
    local("python manage.py dumpdata sites auth.group --indent=1 > ./initial_data.json")
    directories = ""
    for app in DATA_MODELS:
        model_labels = []
        fixtures_dir = "./%s/fixtures" % (app)
        if not os.path.exists(fixtures_dir):
            os.makedirs(fixtures_dir)
        directories += "%s/* " % fixtures_dir
        with fabric_settings(warn_only=True):
            local("mkdir %s" % (fixtures_dir))
        for model in DATA_MODELS[app]:
            model_labels.append("%s.%s" % (app, model))
        local("python manage.py dumpdata %s --indent=1 > %s/initial_data.json" % (" ".join(model_labels), fixtures_dir))
    local("python copy_media.py out")
    local("python manage.py dumpdata --indent=1 --exclude contenttypes --exclude auth.permission > ./initial_data.json")