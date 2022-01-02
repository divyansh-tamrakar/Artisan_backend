from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserForm(models.Model):

    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, unique=True)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
