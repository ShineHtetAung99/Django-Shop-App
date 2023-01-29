from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('shopapp/', views.dashboard,name='dashboard'),
    path('shopapp/customer/', views.customer,name='customers'),
    path('shopapp/customers/<int:id>', views.customers,name='customer.show'),
    path('shopapp/customers/create/', views.customerCreate,name='customer.create'),
    path('shopapp/customers/update/<int:id>', views.customerUpdate,name='customer.update'),
    path('shopapp/customers/delete/<int:id>', views.customerDelete,name='customer.delete'),
    path('shopapp/products/create/', views.productCreate,name='product.create'),
    path('shopapp/products/update/<int:id>', views.productUpdate,name='product.update'),
    path('shopapp/products/delete/<int:id>', views.productDelete,name='product.delete'),
    path('shopapp/products/', views.products,name='products'),
    path('shopapp/orders/', views.orders,name='orders'),
    path('shopapp/order/create/<int:customerId>', views.orderCreate,name='order.create'),
    path('shopapp/order/update/<int:orderId>', views.orderUpdate,name='order.update'),
    path('shopapp/order/delete/<int:orderId>', views.orderDelete,name='order.delete'),
    path('shopapp/tags/', views.tags,name='tags'),
    path('shopapp/tags/create/', views.tagCreate,name='tag.create'),
    path('shopapp/tags/update/<int:id>', views.tagUpdate,name='tag.update'),
    path('shopapp/tags/delete/<int:id>', views.tagDelete,name='tag.delete'),
]