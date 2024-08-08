from django.db import models
from django.contrib.auth.models import AbstractUser 


class CustomUser(AbstractUser): 
   
    HOD = '1'
    STAFF = '2'
    STUDENT = '3'
      
    EMAIL_TO_USER_TYPE_MAP = { 
        'hod': HOD, 
        'staff': STAFF, 
        'student': STUDENT 
    } 
  
    user_type_data = ((HOD, "HOD"), (STAFF, "Staff"), (STUDENT, "Student")) 
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10) 


class Course(models.Model): 
    id = models.AutoField(primary_key=True) 
    course_name = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    


class Student(models.Model): 
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50) 
    profile_pic = models.FileField() 
    address = models.TextField() 
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=1) 
    updated_at = models.DateTimeField(auto_now=True)


class Staff(models.Model): 
    id = models.AutoField(primary_key=True) 
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE) 
    address = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    