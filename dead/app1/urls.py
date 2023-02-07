from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('gifts', views.gifts),
    path('basket', views.basket),
    path('filter/', views.FilterGiftsView, name='filter'),
]
