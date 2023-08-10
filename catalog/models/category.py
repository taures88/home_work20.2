from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}

NOT_NULLABLE = {
    'null': False,
    'blank': False
}


class Category(models.Model):
    name = models.CharField(max_length=50, **NOT_NULLABLE)
    desc = models.TextField(**NULLABLE)

    def __str__(self):
        return f'{self.name} : {self.desc}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)