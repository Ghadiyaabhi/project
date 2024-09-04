from rest_framework import serializers
from .models import Students


class StudentsSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Students
        fields = '__all__' 
        

# class PrincipleSerialzer(serializers.ModelSerializer):
#     class Meta:
#         model = Principle
#         fields = "__all__"        


# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = "__all__"