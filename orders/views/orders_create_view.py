from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db import transaction
from orders.forms import OrderForm, OrderItemInlineFormset
from orders.models.order import Order


class OrdersCreateView(CreateView):
    """
    Создает новые объекты заказа и содержимого заказа
    и выводит шаблон с формой и формсетом
    """

    model = Order
    form_class = OrderForm
    template_name = 'orders/orders_create.html'
    success_url = reverse_lazy('orders:orders_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        formset = self.kwargs.get('order_items_formset', OrderItemInlineFormset())
        context['order_items_formset'] = formset

        return context

    @transaction.atomic
    def form_valid(self, form):
        self.object = form.save(commit=False)
        formset = OrderItemInlineFormset(self.request.POST, instance=self.object)

        if formset.is_valid():
            self.object.save()
            formset.save()
            return HttpResponseRedirect(self.success_url)

        self.kwargs['order_items_formset'] = formset
        return self.form_invalid(form)
