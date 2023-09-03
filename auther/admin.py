from django.contrib import admin
from  .models import AutherModel, AutherBookModel
# Register your models here.
class AutherAdmin(admin.ModelAdmin):
    list_display= ['first_name','last_name','date_of_brth','place_of_birth','Date_of_death','Place_of_death','images','bio','genre']
    search_fields = ['first_name','']
    
admin.site.register(AutherModel,AutherAdmin)


class AutherBooksAdmin(admin.ModelAdmin):
    list_display = ['name','pages','year','price','genre','images','bio']
    search_fields = ['name','genre']

admin.site.register(AutherBookModel,AutherBooksAdmin) 