from django.conf.urls import handler400, handler500
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('future/', views.future, name="future"),
    path('customer_feedback/', views.customer_feedback, name="customer_feedback"),
    path('weather_app/', views.weather_app, name="weather_app"),
]
