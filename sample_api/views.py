from django.http import response
from rest_framework import generics
from .serializers import StudentSerializer
from rest_framework.response import Response

class Student(generics.GenericAPIView):
    serializer_class = StudentSerializer
    def get(self, request):
        return Response ('anil')