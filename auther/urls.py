from django.urls import path
from .views import (AutherGet,AutherCreate, AutherUpdate,AutherDelete,
                    AutherBookGet,AutherBookCreate,AutherBookUpdate,AutherBookDelete)

urlpatterns = [
    #  Auther api
    path('get/', AutherGet.as_view(),name='get_auther'),
    path('create/',AutherCreate.as_view(), name='create_auther'),
    path('update/<int:pk>',AutherUpdate.as_view(),name='update_auther'),
    path('delete/<int:pk>',AutherDelete.as_view(),name='delete_auther'),
    
    #  Auther book  api
    path('book/get/', AutherBookGet.as_view(),name='get_auther_book'),
    path('book/create/',AutherBookCreate.as_view(), name='create_auther_book'),
    path('book/update/<int:pk>',AutherBookUpdate.as_view(),name='update_auther_book'),
    path('book/delete/<int:pk>',AutherBookDelete.as_view(),name='delete_auther_book'),
]
