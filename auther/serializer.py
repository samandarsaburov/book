from rest_framework.serializers import ModelSerializer
from .models import AutherBookModel, AutherModel

class AutherSerializer(ModelSerializer):
    class Meta:
        model = AutherModel
        fields = ('id','first_name','last_name','date_of_brth','place_of_birth','Date_of_death','Place_of_death','images','bio','genre')

class AutherBookSerializer(ModelSerializer):
    class Meta:
        model = AutherBookModel
        fields = ('id','name','pages','year','price','genre','images','bio')