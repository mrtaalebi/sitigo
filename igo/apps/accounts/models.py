from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', null=True)



