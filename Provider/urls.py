from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.providersignin,name='providersignin'),
    path('providersignup/',views.providersignup,name='providersignup'),
    path('forgotpro/',views.forgotpro,name='forgotpro'),
    path('indexprovider/',views.indexprovider,name='indexprovider'),
    path('addvehicle_pro/',views.addvehicle_pro,name='addvehicle_pro'),
    path('vehiclelist/', views.vehiclelist, name='vehiclelist'),
    path('allbookings_pro/',views.allbookings_pro,name='allbookings_pro'),
    path('todaybookings_pro/',views.todaybookings_pro,name='todaybookings_pro'),
    path('pwold/', views.pwold, name='pwold'),
    path('pwnew/',views.pwnew,name='pwnew'),
    path('provider_profile/', views.provider_profile, name='provider_profile'),
    path('logout_pro/', views.logout_pro1, name='logout_pro1'),
    path('load_sub/', views.load_sub, name='load_sub'),
    path('ajax/load-sub/', views.load_sub, name='ajax_load_cities')
]