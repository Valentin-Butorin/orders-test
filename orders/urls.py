from django.urls import path
from orders.views.orders_create_view import OrdersCreateView
from orders.views.orders_list_view import OrdersListView
from orders.views.orders_detail_view import OrdersDetailView
from orders.views.product_type_view import ProductTypeView


app_name = 'orders'

urlpatterns = [
    path('', OrdersListView.as_view(), name='orders_list'),
    path('create/', OrdersCreateView.as_view(), name='orders_form'),
    path('<int:pk>/', OrdersDetailView.as_view(), name='orders_detail'),
    path('product_type/<int:pk>/', ProductTypeView.as_view()),
]
