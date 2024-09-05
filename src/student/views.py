# # from .models import Students
# from rest_framework.views import View
# from rest_framework.response import Response
# from rest_framework import authentication,permissions
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from .serializer import StudentsSerializer

# class StudentDetailView(APIView):
#     # permission_classes = (IsAuthenticated,)

#     def post(self, request):
#         # Assuming 'name' and 'age' are fields in the Students model
#         name = request.data.get('name')
#         age = request.data.get('age')
#         gender = request.data.get('gender')

#         if not name or not age or not gender:
#             return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

#         Create = Students.objects.create(name=name, age=age, gender=gender)
#         return Response({'message': 'Student created successfully'}, status=status.HTTP_201_CREATED)
    



# class StudentDetailUpdateView(APIView):
    
#     def put(self, request, pk):
#         try:
#             student = Students.objects.get(pk=pk)
#         except Students.DoesNotExist:
#             return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = StudentsSerializer(student, data=request.data, partial=True)  
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# class StudentDeleteView(APIView):
#     def delete(self, request, pk):
#         try:
#             student = Students.objects.get(pk=pk)
#         except Students.DoesNotExist:
#             return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    



# class PrincipleCreateView(APIView):
#     def post(self, request): 
#         name = request.data.get('name')
#         age = request.data.get('age')
#         gender = request.data.get('gender')

        
#         if not name or not age or not gender:
#             return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
#         principle = Principle.objects.create(name=name, age=age, gender=gender)
#         return Response({'message': 'Principle created successfully'}, status=status.HTTP_201_CREATED)
    



# class PrincipleUpdateView(APIView):
#     def put(self, request, pk):
#         try:
#             principle = Principle.objects.get(pk=pk)
#         except Principle.DoesNotExist:
#             return Response({'error': 'Principle not found'}, status=status.HTTP_404_NOT_FOUND)
        
        