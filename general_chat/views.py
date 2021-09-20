from django.shortcuts import render
from chatterbot import ChatBot
from django.http import HttpResponse
from django.views import View
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class QuestionView(View):
    def post(self, request, *args, **kwargs):
        response = talk(request.POST['question'])

        return HttpResponse(response, 200)

chatbot = ChatBot('Lyra')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def talk(msg):
    return chatbot.get_response(msg)



