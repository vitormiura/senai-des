from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_index, name = 'homeindex'),
    path('detalhes/<int:id>', views.home_detalhes, name = 'homedetalhes'),
]
