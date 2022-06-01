from django.db import models


class ProductType(models.Model):
    """
    Класс для описания модели типа товара
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Тип товара',
    )

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'

    def __str__(self):
        return self.name
