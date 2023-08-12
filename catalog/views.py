from django.shortcuts import render

from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Иномарка З/Ч'
    }
    return render(request, 'main/index.html', context)

def product(request):
    context = {
        'object_list': Product.objects.all(),
    }
    return render(request, 'main/product.html', context)




def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) {message}')
    return render(request, 'main/contacts.html')