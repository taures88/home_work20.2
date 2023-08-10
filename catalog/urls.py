from django.urls import path

from catalog import views
from catalog.views import index


urlpatterns = [
    path('', index),
    path('contacts/', views.contacts, name='contacts')

    ]