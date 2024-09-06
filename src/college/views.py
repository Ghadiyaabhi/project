from django.shortcuts import render

# Create your views here.
from college.models import Student
from rest_framework.views import APIView
from django.http import HttpResponse
from college.serializer import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated





class StudentDetailView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        student = Student.objects.get(id=request.user.id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    

class StudentUpdateView(APIView):
    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class StudentDeleteView(APIView):
    def delete(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    