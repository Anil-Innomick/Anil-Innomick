from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sample_api.views import Student

urlpatterns = [
    path('student', Student.as_view()),
    
]