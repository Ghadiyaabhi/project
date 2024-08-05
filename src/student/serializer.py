from .models import Students,Courses
from rest_framework import serializers


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


class coursesserializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"