from django.db import models

from catalog.models.products import Product

NULLABLE = {
    'null': True,
    'blank': True
}

NOT_NULLABLE = {
    'null': False,
    'blank': False
}


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    num_version = models.IntegerField(verbose_name='номер версии', **NULLABLE)
    name_version = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название версии')
    current_version = models.BooleanField(**NULLABLE, default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.name_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
