from django.views.generic import RedirectView
from django.urls import reverse


class OrdersRedirectView(RedirectView):
    """
    Перенаправляет на список моделей Delivery
    """
    permanent = False
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        return reverse('orders:orders_list')
