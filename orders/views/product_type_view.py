from django.views.generic import DetailView
from django.http import JsonResponse
from orders.models.product import Product


class ProductTypeView(DetailView):
    """
    Отдаёт наименование типа продукта по его id
    """

    model = Product

    def get(self, request, pk, *args, **kwargs):
        product = self.get_object()
        return JsonResponse(
            {'product_type_name': product.product_type.name},
            status=200,
        )
