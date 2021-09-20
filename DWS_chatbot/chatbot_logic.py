# from DWS_chatbot.forms import ChatBotForm
import json
from datetime import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



with open('QnA_options.json', 'r') as jfile:
        qa_data = jfile.read()
    
qa_json = json.loads(qa_data)
train = []

for k, r in enumerate(qa_json):
    train.append(r['question'])
    train.append(r['answer'])

weather_chatbot = ChatBot('WeatherBot')
trainer = ListTrainer(weather_chatbot)
trainer.train(train)

def talk(msg):
    return weather_chatbot.get_response(msg)
