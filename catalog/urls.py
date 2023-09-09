from django.urls import path
from django.views.decorators.cache import cache_page

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ProductDetailView

app_name = CatalogConfig.name
urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('product/<int:pk>/', cache_page(60)(ProductListView.as_view()), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/detail', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('contacts/', views.contacts, name='contacts')
    ]