from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('filter/', views.FilterGiftsView.as_view(), name='filter'),
    path('gifts', views.gifts),
    path('basket', views.basket),
]
