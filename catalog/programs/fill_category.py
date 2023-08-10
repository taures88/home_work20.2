from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    list_category = [
        {'name': 'запчасти', 'desc': 'шаровая опора'},
        {'name': 'запчасти', 'desc': 'подшипник'},
        {'name': 'АКБ', 'desc': 'кальциевый'},
        {'name': 'АКБ', 'desc': 'гелевый'},
        {'name': 'АКБ', 'desc': 'щелочной'},
    ]

    for item in list_category:
        Category.objects.create(**item)
