from django.urls import path

from catalog import views
from catalog.views import index, product

urlpatterns = [
    path('', index),
    path('product/', product, name='product'),
    path('contacts/', views.contacts, name='contacts')

    ]