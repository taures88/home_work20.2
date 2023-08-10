from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}

NOT_NULLABLE = {
    'null': False,
    'blank': False
}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование', **NOT_NULLABLE)
    desc = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='product/', **NULLABLE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0, **NOT_NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, **NOT_NULLABLE)
    update_at = models.DateTimeField(auto_now=True, **NOT_NULLABLE)

    def __str__(self):
        return f'{self.name} : {self.desc}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('price',)


