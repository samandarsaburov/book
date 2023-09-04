from django.contrib import admin
from .models import BookModel
from modeltranslation.admin import TranslationAdmin
# Register your models here.
class BookModelAdmin(TranslationAdmin):
    pass
    list_display = ['title','pages','year','price','genre','images','auther','bio']
    search_fields = ['title','auther','genre']
    
admin.site.register(BookModel,BookModelAdmin)