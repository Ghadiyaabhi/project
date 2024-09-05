from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Course(models.Model):
    name = models.CharField(max_length=100)
    

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name) + " | " + str(self.address)