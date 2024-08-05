from django.db import models


class Courses(models.Model): 
    id = models.AutoField(primary_key=True) 
    course_name = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager() 

    
class Students(models.Model): 
    id = models.AutoField(primary_key=True) 
    gender = models.CharField(max_length=50) 
    profile_pic = models.FileField() 
    address = models.TextField() 
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING, default=1) 
    updated_at = models.DateTimeField(auto_now=True)


    