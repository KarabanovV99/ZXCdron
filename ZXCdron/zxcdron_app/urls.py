from django.urls import path
from . import views

urlpatterns = [
    path('', views.drone_delivery_home, name='home'),
    path('create_order/thanks', views.success, name='thanks'),
    path('about_us', views.drone_delivery_about_us, name='o_nas'),
    path('with_who', views.drone_delivery_with_who, name='s_kem'),
    path('order', views.drone_delivery_order, name='zakaz'),
    path('employee/control/', views.employee, name='control'),
]
