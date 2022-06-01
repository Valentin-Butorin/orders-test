from django import forms
from datetime import date
from .models.order import Order
from .models.order_item import OrderItem


class OrderForm(forms.ModelForm):
    """
    Форма для ввода информации о доставке
    """

    class Meta:
        model = Order
        fields = ('delivery_office', 'delivery_date', 'file',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        delivery_date_field = self.fields['delivery_date']
        if delivery_date_field:
            delivery_date_field.widget.input_type = 'date'
            delivery_date_field.widget.attrs['value'] = date.today


class OrderItemForm(forms.ModelForm):
    """
    Форма для ввода адреса пункта выдачи
    """

    class Meta:
        model = OrderItem
        fields = ('product',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['product'].widget.attrs['required'] = True


# Формсет для позиций заказа
OrderItemInlineFormset = forms.inlineformset_factory(
    Order,
    OrderItem,
    OrderItemForm,
    min_num=1,
    extra=0,
)
