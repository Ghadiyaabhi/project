from django.db import models
from django.contrib.auth.models import User


class Students(models.Model):

    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    address = models.TextField()
    
