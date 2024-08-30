from .views import StudentDetailView
from django.urls import path



urlpatterns = [
    path('create', StudentDetailView.as_view(),name='student-create'),
    
]
