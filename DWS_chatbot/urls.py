from django.urls import path
from . import views
# from .views import QuestionView

app_name = 'DWS_chatbot'
urlpatterns = [
    # path('chatbot/', QuestionView.as_view(), name='question'),
    path('chatbot/', views.chatbot, name='chatbot'),
]
