from django import forms
from myBot.models import Bot,Part,Controler

class selectBot(forms.Form):
    bot = forms.CharField(label='Choisissez un robot')

class BotAddForm(forms.ModelForm):
    class Meta:
        model = Bot
        exclude = ['reg_date']
        
class PartAddForm(forms.ModelForm):
    class Meta:
        model = Part 
        fields = '__all__' 
        
class ControlerAddForm(forms.ModelForm):
    class Meta:
        model = Controler 
        fields = '__all__'      