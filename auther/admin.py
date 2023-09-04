from django.contrib import admin
from  .models import AutherModel, AutherBookModel
from modeltranslation.admin import TranslationAdmin
# Register your models here.


# Auther   Admin
class AutherAdmin(TranslationAdmin):
    pass
    list_display= ['first_name','last_name','date_of_brth','place_of_birth','Date_of_death','Place_of_death','images','bio','genre']
    search_fields = ['first_name','']
    
admin.site.register(AutherModel,AutherAdmin)



#  Auther book Admin
class AutherBooksAdmin(TranslationAdmin):
    pass 
    list_display = ['name','pages','year','price','genre','images','bio']
    search_fields = ['name','genre']

admin.site.register(AutherBookModel,AutherBooksAdmin) 