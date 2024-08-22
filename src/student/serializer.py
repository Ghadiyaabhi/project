from rest_framework import serializers
from .models import Students


class Students(serializers.Modelseriallizer):
    class Meta:
        model = Students
        fields = '__all__'
        