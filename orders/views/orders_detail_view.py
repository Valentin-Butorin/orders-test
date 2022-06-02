from django.views.generic import DetailView
from orders.models.order import Order


class OrdersDetailView(DetailView):
    """
    Выводит подробную информацию о заказе
    """

    model = Order
    template_name = 'orders/orders_detail.html'
