from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from xml.etree.ElementInclude import include

router = DefaultRouter()
router.register('aval', views.aval_list, basename='avals')
router.register('produtos', views.produtos, basename='prods')
router.register('pedido', views.Pedido, basename='pedido')
router.register('cliente', views.Cliente, basename='cliente')
router.register('item', views.Item, basename='cliente')

# urlpatterns = [
#     path('produtos/', views.produtos_listar),
#     path('produtos/<int:id>/', views.produto_detalhes),
#     path('clientes/', views.ClientList.as_view()),
#     path('clientes/<int:pk>', views.ClientDetail.as_view()),
#     path('pedidos/', views.PedidoList.as_view()),
#     path('pedidos/<int:pk>', views.PedidoDetail.as_view()),
#     path('pedidos/item/', views.ItemList.as_view()),
#     path('pedidos/item/<int:pk>', views.ItemDetail.as_view()),
#     path('avals/', views.aval_list),
#     path('avalsvs/', views.aval_list),
# ]

urlpatterns = router.urls
