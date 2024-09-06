from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=100)



class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_id = models.IntegerField()