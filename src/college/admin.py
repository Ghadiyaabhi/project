from django.contrib import admin

# Register your models here.
from college.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('name','gender','age','address' )
                    