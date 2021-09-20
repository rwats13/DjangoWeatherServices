# from DWS_chatbot.forms import ChatBotForm
from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request as urlb
import requests
from datetime import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from .chatbot_logic import talk
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .forms import ChatBotForm

# Create your views here.


# class QuestionView(View):
#     def post(self, request, *args, **kwargs):
#         response = talk(request.POST['question'])

#         return HttpResponse(response, 200)

@method_decorator(csrf_exempt, name='dispatch')
def chatbot(request):
    question = ''
    answer = ''
    if request.POST:
        form = ChatBotForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            if question[0:15] == 'temperature in ':
                cityname = question[15:]
                resp = urlb.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=45aae1ed72fe61ec3dee566d265dc3f9&units=metric').read()
                json_data = json.loads(resp)
                temp_data = str(json_data['main']['temp'])
                answer = "The current temperature in " + cityname + " is " + temp_data + "°C."
            elif question[0:12] == 'humidity in ':
                cityname = question[12:]
                resp = urlb.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=45aae1ed72fe61ec3dee566d265dc3f9&units=metric').read()
                json_data = json.loads(resp)
                humidity_data = str(json_data['main']['humidity'])
                answer = "The humidity in " + cityname + " is " + humidity_data + "%."
                # Below make general weather, where it tells you sunny, rainy, etc. + could add extra message, e.g. rainy = bring an umbrella, sunny = slip slop slap!
            elif question[0:12] == 'weather in ':
                cityname = question[12:]
                resp = urlb.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=45aae1ed72fe61ec3dee566d265dc3f9&units=metric').read()
                json_data = json.loads(resp)
                humidity_data = str(json_data['main']['humidity'])
                answer = "The humidity in " + cityname + " is " + humidity_data + "%."
            else:
                answer = talk(question)
    form = ChatBotForm()
    return render(request, 'chatbot.html', {'user_input_form': form, 'question': question, 'answer': answer})











    # while True:
    #     request = input("You: ")
    #     response = weather_chatbot.get_response(request)
    #     print("WeatherBot: ", response)
    
    # return render(request, 'chatbot.html')




# # From Monday call
# def talk(msg):
#     return chatbot.get_response(msg)

# If user input == Bye:
#   break