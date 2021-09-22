from django.shortcuts import render
import json
import urllib.request as urlb
from datetime import datetime
from .chatbot_logic import talk, qa_data
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import ChatBotForm

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
def chatbot(request):
    question = ''
    answer = ''
    if request.POST:
        form = ChatBotForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            question_words = question.strip("?").split()
            if question in qa_data:
                answer = talk(question)
            
            elif "temperature" in question_words:
                cityname = question_words[-1]
                resp = urlb.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=45aae1ed72fe61ec3dee566d265dc3f9&units=metric').read()
                json_data = json.loads(resp)
                temp_data = json_data['main']['temp']
                feels_like = str(json_data['main']['feels_like'])
                if temp_data >= 27:
                    answer = "The current temperature in " + cityname + " is " + str(temp_data) + "°C, but it feels like " + feels_like + ". It's hot out there!"
                elif temp_data <= 22:
                    answer = "The current temperature in " + cityname + " is " + str(temp_data) + "°C, but it feels like " + feels_like + ". Don't forget a jacket!"
                else:    
                    answer = "The current temperature in " + cityname + " is " + str(temp_data) + "°C, and it feels like " + feels_like + "."
            
            elif "humidity" in question_words:
                cityname = question_words[-1]
                resp = urlb.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=45aae1ed72fe61ec3dee566d265dc3f9&units=metric').read()
                json_data = json.loads(resp)
                humidity_data = str(json_data['main']['humidity'])
                answer = "The humidity in " + cityname + " is " + humidity_data + "%."
            
            elif ("weather" in question_words) or ("located in" in question) or ("I'm in" in question):
                cityname = question_words[-1]
                resp = urlb.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=45aae1ed72fe61ec3dee566d265dc3f9&units=metric').read()
                json_data = json.loads(resp)
                weather_description = str(json_data['weather'][0]['description'])
                if (weather_description == "clear sky") or (weather_description == "sunny"):
                    answer = "The weather in " + cityname + " is " + weather_description + ". Be sure to wear a hat!"
                elif weather_description == "light rain":
                    answer = "The weather in " + cityname + " is " + weather_description + ". You might need an umbrella!"
                elif (weather_description == "overcast clouds") or (weather_description == "scattered clouds") or (weather_description == "broken clouds") or (weather_description == "few clouds"):
                    answer = "The weather in " + cityname + " is " + weather_description + ". Watch for rain just in case."
                else:
                    answer = "The weather in " + cityname + " is " + weather_description + "."
            
            elif "sunrise" in question_words:
                cityname = question_words[-1]
                resp = urlb.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=45aae1ed72fe61ec3dee566d265dc3f9&units=metric').read()
                json_data = json.loads(resp)
                sunrise = datetime.utcfromtimestamp(json_data['sys']['sunrise']).strftime('%H:%M')
                answer = "Sunrise in " + cityname + " is at " + sunrise + ". Rise and shine!"
            
            elif "sunset" in question_words:
                cityname = question_words[-1]
                resp = urlb.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=45aae1ed72fe61ec3dee566d265dc3f9&units=metric').read()
                json_data = json.loads(resp)
                sunset = datetime.utcfromtimestamp(json_data['sys']['sunset']).strftime('%H:%M')
                answer = "Sunset in " + cityname + " is at " + sunset + "."
            
            else:
                answer = "I'm sorry, I don't understand your question. Please ask again."
    form = ChatBotForm()
    return render(request, 'chatbot.html', {'user_input_form': form, 'question': question, 'answer': answer})