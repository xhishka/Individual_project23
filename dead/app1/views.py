from django.shortcuts import render
from .models import Gifts, Basket
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q


def index(request):
    return render(request, 'app1/index.html')


def gifts(request):
    gifts = Gifts.objects.order_by("id")
    return render(request, 'app1/gifts_list.html', {'title': 'Подарки', 'gifts': gifts})


def basket(request):
    basket = Basket.objects.order_by("id")
    return render(request, 'app1/basket.html', {'title': 'Избранное', 'basket': basket})


class Gifts_test:
    """Жанры и года выхода фильмов"""

    def get_whom(self):
        return Gifts.objects.filter.values("whom")

    def get_age(self):
        return Gifts.objects.filter(draft=False).values("age")


class FilterGiftsView(Gifts_test, ListView):
    def get_queryset(self):
        queryset = Gifts.objects.filter(
            Q(whom__in=self.request.GET.getlist("whom")) |
            Q(age__in=self.request.GET.getlist("age")) |
            Q(reason__in=self.request.GET.getlist("reason"))
        )
        return queryset
