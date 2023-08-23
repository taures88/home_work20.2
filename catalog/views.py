from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Category, Product


class CategoryListView(ListView):
    model = Category
    template_name = 'main/index.html'


# def index(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Иномарка З/Ч'
#     }
#     return render(request, 'main/index.html', context)


# def product(request, pk):
#     product_list = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(category_id=pk),
#         'title': product_list.name
#     }
#     return render(request, 'main/product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'main/product.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        product_l = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = product_l.name

        return context_data



def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) {message}')
    return render(request, 'main/contacts.html')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('catalog:category')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'
    success_url = reverse_lazy('catalog:category')


class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:category')


