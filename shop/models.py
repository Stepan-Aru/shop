from django.db import models
from django.urls import reverse


class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    price = models.FloatField(verbose_name='Цена товара')
    on_stock = models.IntegerField(verbose_name='Кол-во на складе')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория товара')
    is_sale = models.BooleanField(default=True, verbose_name='Продажа')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'