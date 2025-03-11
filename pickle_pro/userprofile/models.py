from django.db import models

# Create your models here.
class CustomUser(models.Model):
    full_name = models.CharField(max_length=250,null=True,blank=True)
    