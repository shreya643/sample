from django.urls import path
from . import views

urlpatterns = [
    path('login_buyer/', views.login_buyer, name='login_buyer'),
    path('login_seller/', views.login_seller, name='login_seller'),
    path('register_buyer/', views.register_buyer, name='register_buyer'),
    path('register_seller/', views.register_seller, name='register_seller'),
]
