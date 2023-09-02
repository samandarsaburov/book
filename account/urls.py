from django.urls import path
from .views import Get_all , CreateLogin

urlpatterns = [
    path('get/',Get_all.as_view()),
    path('create/',CreateLogin.as_view(),name='CreateLogin')
]
