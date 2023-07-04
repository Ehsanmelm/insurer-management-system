from django.db import models
from django.conf import settings
from django.contrib import admin

# Create your models here.


class InsurerModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name