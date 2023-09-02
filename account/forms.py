from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser

# create yangi user
class CustomUserCreate(UserCreationForm):
    class Mete(UserCreationForm):
        model = CustomUser
        fields = ('username','first_name','last_name','phone','email','password','roles')
        
        
# create update user
class CustomUserUpdate(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username','first_name','last_name','phone','email','password','roles')