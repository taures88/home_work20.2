from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}

NOT_NULLABLE = {
    'null': False,
    'blank': False
}


class City(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='Содержимое')
    img = models.ImageField(upload_to='city_img/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, **NOT_NULLABLE, verbose_name='Дата создания')
    publication = models.BooleanField(**NULLABLE, default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')



    def __str__(self):
        return f'{self.title} : {self.body}'

    def __repr__(self):
        return 'Image(%s, %s)' % (self.body, self.img)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


