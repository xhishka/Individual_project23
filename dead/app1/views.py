from django.shortcuts import render
from .models import Gifts


def index(request):
    return render(request, 'app1/index.html')


def gifts(request):
    gifts = Gifts.objects.order_by("id")
    return render(request, 'app1/gifts.html', {'title': 'Подарки', 'gifts': gifts})


def basket(request):
    return render(request, 'app1/basket.html')
