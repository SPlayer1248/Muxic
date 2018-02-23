from django.urls import path

from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('add_album/', views.add_album, name='add_album'),
    path('user/', views.user, name='user'),
]
