from django.db import models
from django.contrib.auth import models

class User(models.User):

    def __str__(self):
        return "@{}".format(self.username)