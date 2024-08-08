from django.contrib import admin

from .models import Student,Staff,Course


@admin.register(Student)
class studentsAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('id',  'name','address','gender')

@admin.register(Staff)
class staffAdmin(admin.ModelAdmin):
    model = Staff
    list_display = ('id','admin','created_at')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('id','course_name')
