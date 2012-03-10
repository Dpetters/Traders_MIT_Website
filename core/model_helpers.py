import datetime
import os


def get_image_filename(instance, filename):
    extension = os.path.splitext(filename)[1]
    return "%s/%s_%s%s" % (str(type(instance)._meta).replace(".", "/"), instance.user.username.replace(" ", "_").lower(), datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'), extension)