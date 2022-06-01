from django.db import models
from .product_type import ProductType


class Product(models.Model):
    """
    Класс для описания модели товара
    """

    name = models.CharField(
        max_length=255,
        verbose_name='Наименование товара',
    )
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Тип товара',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
