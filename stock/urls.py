
from django.conf.urls import url

from .views import index

from .views import *




urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^display_products$', display_products, name='display_products'),
    url(r'^display_customers$', display_customers, name="display_customers"),
    url(r'^display_orders$', display_orders, name="display_orders"),

    url(r'^add_products$', add_products, name="add_products"),
    url(r'^add_customers$', add_customers, name="add_customers"),
    url(r'^add_orders$', add_orders, name="add_orders"),

    url(r'^products/edit_item/(?P<pk>\w+)$', edit_products, name="edit_products"),
    url(r'^customers/edit_item/(?P<pk>\w+)$', edit_customers, name="edit_customers"),
    url(r'^orders/edit_item/(?P<pk>\w+)$', edit_orders, name="edit_orders"),

    url(r'^products/delete/(?P<pk>\w+)$', delete_products, name="delete_products"),
    url(r'^customers/delete/(?P<pk>\w+)$', delete_customers, name="delete_customers"),
    url(r'^orders/delete/(?P<pk>\w+)$', delete_orders, name="delete_orders")
]