from django.urls import path

from crud_views.car_model_views import CarModelDetailView, CarModelCreateView, CarModelUpdateView, CarModelDeleteView
from crud_views.customer_views import CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView
from crud_views.order_line_views import OrderLineDetailView, OrderLineCreateView, OrderLineUpdateView, \
    OrderLineDeleteView
from crud_views.service_views import ServiceDetailView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('car_models', views.car_models, name='car_models'),
    path('unauthorized_access/', views.unauthorized_access, name='unauthorized_access'),
    path('car_models/<int:car_model_id>/', CarModelDetailView.as_view(), name='car_model'),
    path('car_models/new', CarModelCreateView.as_view(), name='car-model-new'),
    path('car_models/<int:car_model_id>/update', CarModelUpdateView.as_view(), name='car-model-update'),
    path('car_models/<int:car_model_id>/delete', CarModelDeleteView.as_view(), name='car-model-delete'),
    path('customers', views.customers, name='customers'),
    path('customer/<int:customer_id>/', CustomerDetailView.as_view(), name='customer'),
    path('customer/new', CustomerCreateView.as_view(), name='customer-new'),
    path('customer/<int:customer_id>/update', CustomerUpdateView.as_view(), name='customer-update'),
    path('customer/<int:customer_id>/delete', CustomerDeleteView.as_view(), name='customer-delete'),
    path('services', views.services, name='services'),
    path('services/<int:service_id>/', ServiceDetailView.as_view(), name='service'),
    path('services/new', ServiceCreateView.as_view(), name='service-new'),
    path('services/<int:service_id>/update', ServiceUpdateView.as_view(), name='service-update'),
    path('services/<int:service_id>/delete', ServiceDeleteView.as_view(), name='service-delete'),
    path('order_lines/', views.order_lines, name='order_lines'),
    path('order_line/<int:order_line_id>/', OrderLineDetailView.as_view(), name='order_line'),
    path('order_line/new', OrderLineCreateView.as_view(), name='order_line-new'),
    path('order_line/<int:order_line_id>/update', OrderLineUpdateView.as_view(), name='order_line-update'),
    path('order_line/<int:order_line_id>/delete', OrderLineDeleteView.as_view(), name='order_line-delete'),
    path('myservices/', views.CarServicesByCustomer.as_view(), name='my-services'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
