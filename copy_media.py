import os, shutil
from optparse import OptionParser

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.conf import settings
from django.db import models


def get_filefields(model_cls):
    filefields = []
    for field in model_cls._meta.fields:
        if issubclass(type(field), models.FileField):
            filefields.append(field.name)
    return filefields


def main():
    usage = "usage: %prog [options] in_or_out"
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()
    
    if len(args) != 1:
        parser.error("You must specify whether you want media copied in or out.")
    
    root = settings.PROD_MEDIA_ROOT
    
    model_paths = []
    for m in models.get_models():
        if get_filefields(m):
            model_paths.append("%s/%s" % (m.__module__.split(".")[-2], m._meta.object_name.lower()))
    
    print model_paths

    if args[0] == "in":
        copy_in_media(root, model_paths)
    else:
        copy_out_media(root, model_paths)

    
def delete_contents(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def copy_in_media(root, model_paths):
    if not os.path.exists(root):
        os.makedirs(root)
    for model_path in model_paths:
        data_path = os.path.normpath(root + model_path)
        media_path = os.path.normpath(settings.MEDIA_ROOT + model_path)
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        if os.path.exists(media_path):
            delete_contents(media_path)
            os.rmdir(media_path)
        shutil.copytree(data_path, media_path)


def copy_out_media(root, model_paths):
    if os.path.exists(root):
        delete_contents(root)
    else:
        os.makedirs(root)
    for model_path in model_paths:
        data_path = os.path.normpath(root + model_path)
        media_path = os.path.normpath(settings.MEDIA_ROOT + model_path)
        if not os.path.exists(media_path):
            os.makedirs(media_path)
        shutil.copytree(media_path, data_path)


if __name__ == "__main__":
    main()