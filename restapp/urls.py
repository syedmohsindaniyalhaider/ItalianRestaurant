from . import views
from django.urls import path

app_name = 'restapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('menu-and-pricing/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
]
