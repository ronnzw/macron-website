from django.urls import path

from . import views


app_name = 'website'
urlpatterns = [
    path('',views.home, name='home'),
    path('services/', views.service, name='services'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('careers/', views.careers, name='careers')
]