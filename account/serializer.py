from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','phone','email','password','roles')
    def create(self,validated_date):
        user = CustomUser(
            username = validated_date['username'],
            first_name = validated_date['first_name'],
            last_name = validated_date['last_name'],
            phone = validated_date['phone'],
            email = validated_date['email'],
            roles = validated_date.get('roles',1)
        )
        user.set_password(validated_date['password'])
        user.save()
        return user
        
    # end def