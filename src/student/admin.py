from django.contrib import admin

from .models import Students


@admin.register(Students)
class studentAdmin(admin.ModelAdmin):
    model = Students
    list_display = [
        "id",
        "gender",
        "profile_pic",
        "address",
        
    ]
