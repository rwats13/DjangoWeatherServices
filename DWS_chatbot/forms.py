from django import forms

class ChatBotForm(forms.Form):
    question = forms.CharField(required=True, max_length=1000)
