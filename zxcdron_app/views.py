from django.shortcuts import render
from .models import Order


def drone_delivery(request):
    return render(request, 'zakaz.html')


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
