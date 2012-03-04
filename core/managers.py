from django.db import models

class BoardMemberManager(models.Manager):
    def current(self):
        return self.filter(left__isnull=True)