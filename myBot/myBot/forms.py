from django import forms
from myBot.models import Bot,Part,Controler,Sensor, SensorType,Relay,Servo,ServoType,SpeedClass

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
    
class SensorAddForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = '__all__'
        
class SensorTypeAddForm(forms.ModelForm):
    class Meta:
        model = SensorType
        fields = '__all__'
        
class RelayAddForm(forms.ModelForm):
    class Meta:
        model = Relay
        fields = '__all__' 
        
class ServoAddForm(forms.ModelForm):
    class Meta:
        model = Servo
        fields = '__all__'
        
class ServoTypeAddForm(forms.ModelForm):
    class Meta:
        model = ServoType
        fields = '__all__'
        
class SpeedClassAddForm(forms.ModelForm):
    class Meta:
        model = SpeedClass
        fields = '__all__'