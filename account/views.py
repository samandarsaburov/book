from django.shortcuts import render
from .models import CustomUser
from .serializer import CustomUserSerializer
from rest_framework import generics
# Create your views here.

class Get_all(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
class CreateLogin(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer