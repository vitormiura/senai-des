from cgitb import lookup
from posixpath import basename
from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register('produtos', views.Produtos, basename='produtos')
router.register('avaliacoes', views.aval_list, basename='avaliacoes')
# router.register('pedido', views.Pedido, basename='pedido')
# router.register('cliente', views.Cliente, basename='cliente')
# router.register('item', views.Item, basename='item')
# router.register('item', views.Item, basename='item')
router.register('categoria', views.Categoria, basename='categoria')

produto_router = routers.NestedDefaultRouter(router, 'produtos', lookup='produtos')
produto_router.register('avaliacoes', views.aval_list, basename='avaliacoes')

urlpatterns = router.urls + produto_router.urls

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

# urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls))
# ]