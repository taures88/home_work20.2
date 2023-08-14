from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import index, product

app_name = CatalogConfig.name
urlpatterns = [
    path('', index),
    path('product/<int:pk>/', product, name='product'),




    path('contacts/', views.contacts, name='contacts')

    ]