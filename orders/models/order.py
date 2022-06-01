from django.db import models
from .delivery_office import DeliveryOffice


class Order(models.Model):
    """
    Класс для описания модели заказа
    """

    delivery_office = models.ForeignKey(
        DeliveryOffice,
        on_delete=models.PROTECT,
        verbose_name='Пункт выдачи',
    )
    delivery_date = models.DateField(
        verbose_name='Дата доставки',
    )
    file = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='Файл',
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ № {self.id} (до {self.delivery_date.strftime("%d.%m.%Y")})'
