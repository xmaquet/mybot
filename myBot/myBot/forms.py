from django import forms
from myBot.models import Bot

class selectBot(forms.Form):
    bot = forms.CharField(label='Choisissez un robot')

class BotAddForm(forms.ModelForm):
    class Meta:
        model= Bot
        fields = '__all__'
        