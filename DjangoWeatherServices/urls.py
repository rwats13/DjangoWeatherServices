"""DjangoWeatherServices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('DWS_app.urls', namespace='DWS_app')),
#     path('chatbot/', include('DWS_chatbot.urls', namespace='DWS_chatbot')),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DWS_app.urls', 'DWS_chatbot.urls')),
    path('', include('DWS_chatbot.urls', namespace='DWS_chatbot')),
    # path('general_chat/', include('general_chat.urls')),
    # path('DWS_chatbot/', include('DWS_chatbot.urls')),
]
