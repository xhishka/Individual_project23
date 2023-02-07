from django.shortcuts import render
from .models import Gifts, Basket


def index(request):
    return render(request, 'app1/index.html')


def gifts(request):
    gifts = Gifts.objects.order_by("id")
    return render(request, 'app1/gifts.html', {'title': 'Подарки', 'gifts': gifts})


def basket(request):
    basket = Basket.objects.order_by("id")
    return render(request, 'app1/basket.html', {'title': 'Избранное', 'basket': basket})


class FilterGiftsView(Gifts):
    def get_queryset(self):
        queryset = Gifts.objects.filter(whom__in=self.request.GET.getlist("whom"))
        return queryset
