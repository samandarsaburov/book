from rest_framework.serializers import ModelSerializer
from .models import BookModel

class BookSerializer(ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id','title','pages','year','price','genre','images','auther','bio')