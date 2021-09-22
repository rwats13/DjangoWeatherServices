from django.urls import path
from . import views

app_name = 'DWS_chatbot'
urlpatterns = [
    path('chatbot/', views.chatbot, name='chatbot'),
]
