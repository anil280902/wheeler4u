from django.contrib import admin
from django.urls import path,include
from . import views
from User.views import usersignin

urlpatterns = [
    path('',usersignin,name='usersignin'),
    path('adminsignin/',views.adminsignin,name='adminsignin'),
    path('forgotad/',views.forgotad,name='forgotad'),
    path('indexadmin/',views.indexadmin,name='indexadmin'),
    path('vehiclelist_admin/', views.vehiclelist_admin, name='vehiclelist_admin'),
    path('todaybookings/',views.todaybookings,name='todaybookings'),
    path('allbookings/',views.allbookings,name='allbookings'),
    path('addcat/', views.addcat, name='addcat'),
    path('subcategory/', views.subcategory, name='subcategory'),
    # path('load_sub/', views.load_sub, name='load_sub'),
    path('showcat/', views.showcat, name='showcat'),
    path('showsubcat/', views.showsubcat, name='showsubcat'),
    path('changepw/', views.changepw, name='changepw'),
    path('changepw1/',views.changepw1,name='changepw1'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('logout/', views.logout1, name='logout1'),
    # path('ajax/load-sub/', views.load_sub, name='ajax_load_cities')
]