from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request as urlb
import requests
from datetime import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create your views here.
def chatbot():    
    with open('DWS_chatbot\QnA_options.json', 'r') as jfile:
        qa_data = jfile.read()
    
    qa_json = json.loads(qa_data)
    train = []

    for k, r in enumerate(qa_json):
        train.append(r['question'])
        train.append(r['answer'])
    
    weather_chatbot = ChatBot('Wally')
    trainer = ListTrainer(weather_chatbot)
    trainer.train(train)

    while True:
        request = input("You: ")
        response = weather_chatbot.get_response(request)
        print("Wally: ", response)
    

# # From Monday call
# def talk(msg):
#     return chatbot.get_response(msg)