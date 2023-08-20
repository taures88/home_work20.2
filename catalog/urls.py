from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ProductListView

app_name = CatalogConfig.name
urlpatterns = [
    path('', CategoryListView.as_view()),
    path('product/<int:pk>/', ProductListView.as_view(), name='product'),

    path('contacts/', views.contacts, name='contacts')
    ]