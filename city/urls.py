from django.urls import path


from city.apps import CityConfig
from city.views import CityCreateView, CityListView, CityDetailView, CityUpdateView, CityDeleteView

app_name = CityConfig.name
urlpatterns = [
    path('create/', CityCreateView.as_view(), name='create'),
    path('', CityListView.as_view(), name='list'),
    path('view/<int:pk>/', CityDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', CityUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    ]