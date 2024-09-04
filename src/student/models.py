from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Course(models.Model):
    name = models.CharField(max_length=100)
    
    
    
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    address = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    # course_id = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)


