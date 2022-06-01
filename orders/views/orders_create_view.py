from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from orders.forms import OrderForm, OrderItemInlineFormset


class OrdersCreateView(CreateView):
    """
    Создает новые объекты доставки и адресов пунктов выдачи
    и выводит шаблон с формой и формсетом
    """

    form_class = OrderForm
    template_name = 'orders/orders_create.html'
    success_url = reverse_lazy('orders:orders_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items_formset'] = OrderItemInlineFormset()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = form_class(self.request.POST, self.request.FILES)
        order_items_formset = OrderItemInlineFormset(self.request.POST)
        if form.is_valid() and order_items_formset.is_valid():
            return self.form_valid(form, order_items_formset)
        else:
            return self.form_invalid(form, order_items_formset)

    def form_valid(self, form, order_items_formset):
        order = form.save(commit=False)
        order.save()

        order_items = order_items_formset.save(commit=False)
        for item in order_items:
            item.order = order
            item.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form, order_items_formset):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                order_items_formset=order_items_formset,
            )
        )
