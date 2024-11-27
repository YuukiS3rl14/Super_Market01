from django.urls import path
from .views import *

urlpatterns = [
    path('', showIndex, name='index'),
    path('index/', showIndex, name='index'),
    path('registro/', showRegistro, name='registro'),
    path('search/', showSearch, name='search'),
    path('detail/<int:id>/', showDetail, name='detail'),
    path('contact/', showContact, name='contact'),
    path('aboutus/', showAboutUs, name='aboutus'),
    path('admin/', showAdmin, name='admin'),
    path('add/', addProduct, name='add'),
    path('list/', listProduct, name='list'),
    path('update/<id>/', updateProduct, name='update'),
    path('delete/<id>/', deleteProduct, name='delete'),
    path('favoritos/', showFavorite, name='favoritos'),
    path('favoritos/add/<int:product_id>/', add_favorite, name='add_favorite'),
    path('favoritos/remove/<int:product_id>/', remove_favorite, name='remove_favorite'),
    path('perfil/', editar_perfil, name='perfil'),
]
