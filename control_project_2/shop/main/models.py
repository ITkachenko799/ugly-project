from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse


class Prod(models.Model):
    CATEGORY = [
        ('NOTEBOOK','Ноутбук'),
        ('PHONE', 'Телефоны'),
    ]

    vendor_code = models.CharField(max_length=64, blank=False, unique=True, verbose_name="Поставщик")
    category = models.CharField(
        max_length=10,
        blank=False,
        choices=CATEGORY,
        default='NOTEBOOK',
        verbose_name="Категория товара"
    )

    name_product = models.CharField(max_length=64, blank=False, verbose_name='Название')
    info = models.TextField(blank=True, default='', verbose_name='Описание')
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False, default=0, verbose_name="Цена")
    img = models.ImageField(upload_to='prod_img', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товар'

    def __str__(self):
        return self.category + ' ' + self.name_product


class Sale(models.Model):
    product = models.ForeignKey('Prod',

                                on_delete=models.CASCADE,
                                related_name='sales',
                                related_query_name='product',
                                verbose_name="Товар"
                                )

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Рродажи'

    def __str__(self):
        return f'Продукт:{self.product}'