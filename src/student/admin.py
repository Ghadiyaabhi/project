from django.contrib import admin

from .models import Students


@admin.register(Students)
class studentAdmin(admin.ModelAdmin):
    model = Students
    list_display = ["id","gender","address","name"]


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     model = Course
#     list_display = ["name"]