from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from city.models import City


class CityCreateView(CreateView):
    model = City
    fields = ('title', 'body', 'img')
    success_url = reverse_lazy('city:list')

    def form_valid(self, form):
        if form.is_valid():
            new_city = form.save()
            new_city.slug = slugify(new_city.title)
            new_city.save()

        return super().form_valid(form)


class CityUpdateView(UpdateView):
    model = City
    fields = ('title', 'body', 'img')
    success_url = reverse_lazy('city:list')

class CityListView(ListView):
    model = City
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class CityDetailView(DetailView):
    model = City

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class CityDeleteView(DeleteView):
    model = City
    success_url = reverse_lazy('city:list')
