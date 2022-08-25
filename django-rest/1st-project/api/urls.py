from getpass import getuser
from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.getData),
    path('items/add/', views.addItem),
    path('users/add/', views.addUser),
    path('users/', views.getUser),
]