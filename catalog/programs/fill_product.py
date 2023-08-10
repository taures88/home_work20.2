from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    list_products = [
        {'name': 'Zekkert', 'desc': 'шаровая опора', 'category_id': 'запчасти', 'price': '1200'},
        {'name': 'SKF', 'desc': 'подшипник', 'category_id': 'запчасти', 'price': '2300'},
        {'name': 'Bosch', 'desc': 'кальциевый', 'category_id': 'АКБ', 'price': '3000'},
        {'name': 'BMW', 'desc': 'гелевый', 'category_id': 'АКБ', 'price': '4000'},
        {'name': 'TAB', 'desc': 'щелочной', 'category_id': 'АКБ', 'price': '2500'},

    ]
    for item in list_products:
        Product.objects.create(**item)
