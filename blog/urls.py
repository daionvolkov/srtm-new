from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('search_code/', views.search_code, name='search_code'),
    path('order/', views.order, name='order'),
    path('mail_send/', views.mail_send, name='mail_send'),
    path('contactus/', views.ContactUs, name='contactus'),
    path('fororder/', views.fororder, name='fororder'),
    path('proezd', views.proezd, name='proezd'),
    path('photos', views.photos, name='photos'),
    path('sendbid/', views.sendbid, name='sendbid'),
    path('ordersend/', views.ordersend, name='ordersend'),

    #path('order_send/', views.order_send, name='order_send'),
    ]
