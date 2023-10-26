from django.shortcuts import render


def drone_delivery(request):
    return render(request, 'main.html')
