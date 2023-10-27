from django.shortcuts import render
from .models import Order


def drone_delivery_home(request):
    return render(request, 'Main1.html')


def drone_delivery_about_us(request):
    return render(request, 'O_NAS.html')


def drone_delivery_with_who(requests):
    return render(requests, 'S_KEM.html')


def drone_delivery_order(requests):
    return render(requests, 'zakaz.html')


def success(request):
    if request.method == 'POST':
        order = Order()
        data = {
            'address': request.POST['address'],
            'full_name': request.POST['full_name'],
            'phone': request.POST['phone'],
            # 'time': request.GET['time'],
        }

        order.address = data['address']
        order.receiver_name = data['full_name']
        order.phone = data['phone']
        order.save()

    return render(request, 'success.html')

def for_employee_auth(requests):
    return render(requests, )
