from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.usersignin,name='usersignin'),
    path('usersignup/',views.usersignup,name='usersignup'),
    path('indexuser/',views.indexuser,name='indexuser'),
    path('cars/', views.cars, name='cars'),
    path('car_details/<str:id>', views.car_details, name='car_details'),
    path('booking_info/<str:id>', views.booking_info, name='booking_info'),
    path('payment/', views.payment, name='payment'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_u, name='logout_u'),
]