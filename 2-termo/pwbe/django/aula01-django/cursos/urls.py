from urllib.parse import urlparse
from django.urls import path    
from . import views

urlpatterns=[
    path("", views.index, name = 'index'),
    # path("curso", views.cursos, name = 'curso'),
    path("<int:curso_id>", views.cursos, name = 'curso'),
]