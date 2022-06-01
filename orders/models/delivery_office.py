from django.db import models


class DeliveryOffice(models.Model):
    """
    Класс для описания модели пункта выдачи
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Название пункта выдачи',
    )
    address = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Адрес пункта выдачи',
    )

    class Meta:
        verbose_name = 'Пункт выдачи'
        verbose_name_plural = 'Пункты выдачи'

    def __str__(self):
        return f'{self.name} ({self.address})'
