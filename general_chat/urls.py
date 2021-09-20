from django.urls import path
from .views import QuestionView

urlpatterns = [
    path('chatbot/', QuestionView.as_view(), name='question'),
]