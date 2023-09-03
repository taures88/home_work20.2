from django.contrib import admin

from catalog.models import Category, Product
from catalog.models.version import Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name', 'price',)
    list_filter = ('created_at',)
    search_fields = ('name', 'desc',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'desc',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name_version', 'num_version', 'current_version',)
    list_filter = ('name_version',)