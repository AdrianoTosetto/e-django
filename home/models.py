from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

from django.db import models

# Create your models here.

class AppUser(models.Model):
	first_name = models.CharField(max_length=30)
	image_url  = models.CharField(max_length=255, default = 'default.png')

class AppMessage(models.Model):
	whoSent = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name = 'whoSent')
	whoRecv = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name = 'whoRecv')
	msg     = models.CharField(max_length = 200)
	read    = models.BooleanField(default = False)