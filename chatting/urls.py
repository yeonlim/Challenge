from django.urls import path, include
from .views import *


urlpatterns = [
   path('', chatting, name='chatting'),
   path('write/', chatting_write, name='chatting_write'),
   path('send/', chatting_send, name='chatting_send'),
   path('write/userlist', chatting_userlist, name='chatting_userlist'),
   path('detail/<str:id>', chatting_detail, name='chatting_detail'),
   path('delete/<str:id>', chatting_delete, name='chatting_delete'),

]