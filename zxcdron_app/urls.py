from django.urls import path
from . import views

urlpatterns = [
    path('', views.drone_delivery, name='page_of_delivery'),
]
