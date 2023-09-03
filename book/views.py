from django.shortcuts import render
from .models import BookModel
from .serializer import BookSerializer
from rest_framework import generics

# Create your views here.

class GetAll(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    
class Create(generics.CreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    
class Update(generics.UpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

class Delete(generics.DestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer