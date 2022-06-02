from django.db import models
from .product import Product
from .order import Order


class OrderItem(models.Model):
    """
    Класс для описания позиции в заказе
    """

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ',
        related_name='order_items')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт')
