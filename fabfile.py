from fabric.api import local
from fabric.contrib import django as fabric_django

fabric_django.settings_module('settings')

__all__= ["commit_data", "load_data"]

def load_data():
    local("python copy_media.py in")
    local("python manage.py loaddata ./initial_data.json")
                
def commit_data():
    local("python copy_media.py out")
    local("python manage.py dumpdata --indent=1 --exclude contenttypes > ./initial_data.json")
