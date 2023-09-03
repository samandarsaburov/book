from django.contrib import admin
from .models import BookModel
# Register your models here.
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title','pages','year','price','genre','images','auther','bio']
    search_fields = ['title','auther','genre']
    
admin.site.register(BookModel,BookModelAdmin)