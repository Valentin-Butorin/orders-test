from django.views.generic import ListView
from orders.models.order import Order


class OrdersListView(ListView):
    """
    Выводит список заказов
    """

    model = Order
    template_name = 'orders/orders_list.html'
