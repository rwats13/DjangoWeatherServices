from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request as urlb
import requests
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def future(request):
    return render(request, 'future.html')

def customer_feedback(request):
    return render(request, 'customer_feedback.html')

def weather_app(request):
    data_response = {}
    if request.method == 'POST':
        lat     = request.POST['latitude']
        long    = request.POST['longitude']
        if lat != '' and long != '':
            if -90.0 < float(lat) < 90.0 and -180.0 < float(long) < 180.0:
                resp    = urlb.urlopen(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=45aae1ed72fe61ec3dee566d265dc3f9&units=metric').read()
                json_data = json.loads(resp)
                data_response = {
                    'location'  : json_data['name'],
                    'descrip'   : (json_data['weather'][0]['description']).capitalize(),
                    'crnt_temp' : str(json_data['main']['temp'])+'°C',
                    'min_temp'  : str(json_data['main']['temp_min'])+'°C',
                    'max_temp'  : str(json_data['main']['temp_max'])+'°C',
                    'humidity'  : str(json_data['main']['humidity'])+"%",
                    'sunrise'   : datetime.utcfromtimestamp(json_data['sys']['sunrise']).strftime('%H:%M'),
                    'sunset'    : datetime.utcfromtimestamp(json_data['sys']['sunset']).strftime('%H:%M'),
                }
            else:
                data_response = {
                    'error_message': 'Invalid input! Try using a latitude between -90 and 90, and a longitude between -180 and 180.'
                }
    return render(request, 'weather_app.html', data_response)
