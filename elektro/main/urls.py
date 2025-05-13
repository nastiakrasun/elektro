from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_reading, name='submit_reading'),
    path('success/', views.success, name='success'),
    path('tariffs/', views.tariffs, name='tariffs'),
    path('bills/', views.bills, name='bills'),
    path('meters/', views.meters, name='meters'),
]