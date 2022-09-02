from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.produtos_listar),
    path('produtos/<int:id>/', views.produto_detalhes),
    path('clientes/', views.ClientList.as_view()),
    path('clientes/', views.ClientList.as_view()),
    path('clientes/<int:pk>', views.ClientDetail.as_view()),
    path('pedidos/', views.PedidoList.as_view()),
    path('pedidos/<int:pk>', views.PedidoDetail.as_view()),
    path('pedidos/item/', views.ItemList.as_view()),
    path('pedidos/item/<int:pk>', views.ItemDetail.as_view()),
]
