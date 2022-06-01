from django.contrib import admin
from .models.product import Product
from .models.product_type import ProductType
from .models.delivery_office import DeliveryOffice
from .models.order_item import OrderItem
from .models.order import Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(DeliveryOffice)
class DeliveryOfficeAdmin(admin.ModelAdmin):
    pass


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    can_delete = False
    max_num = 0
    fields = ('product',)
    readonly_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemTabularInline,)
