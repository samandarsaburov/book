from django.shortcuts import render
from .models import AutherModel, AutherBookModel
from .serializer import AutherSerializer, AutherBookSerializer
from rest_framework import generics
# Create your views here.

# Auther  API lari  

class AutherGet(generics.ListAPIView):
    queryset = AutherModel.objects.all()
    serializer_class = AutherSerializer
    
class AutherCreate(generics.CreateAPIView):
    queryset = AutherModel.objects.all()
    serializer_class = AutherSerializer

class AutherUpdate(generics.UpdateAPIView):
    queryset = AutherModel.objects.all()
    serializer_class = AutherSerializer
    
class AutherDelete(generics.DestroyAPIView):
    queryset = AutherModel.objects.all()
    serializer_class = AutherSerializer
    

# Auther book API lari

class AutherBookGet(generics.ListAPIView):
    queryset = AutherBookModel.objects.all()
    serializer_class = AutherBookSerializer
    
class AutherBookCreate(generics.CreateAPIView):
    queryset = AutherBookModel.objects.all()
    serializer_class = AutherBookSerializer


class AutherBookUpdate(generics.UpdateAPIView):
    queryset = AutherBookModel.objects.all()
    serializer_class = AutherBookSerializer


class AutherBookDelete(generics.DestroyAPIView):
    queryset = AutherBookModel.objects.all()
    serializer_class = AutherBookSerializer