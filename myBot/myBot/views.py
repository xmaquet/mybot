
from django.shortcuts import render,redirect
from myBot.models import Bot, Part, Controler,ControlerType, ServoType, SpeedClass, SensorType, Servo, Relay, Sensor
from datetime import datetime
    
def selectBot(request):
    bots = Bot.objects.all()
    if 'logged_bot_id' in request.session:
        botId = request.session['logged_bot_id']
        bot = Bot.objects.filter(id=botId)
        if bot:
            return render(request, 'selectBot.html',
                      {'listBots':bots,
                       'bot':bot},
                      )
        else:
            if bots:
                return render(request,'selectBot.html',
                              {'listBots':bots})
            else:
                return render(request,'selecBot.html')
    
    else:
        if bots:
            return render(request,'selectBot.html',
                              {'listBots':bots})
        else:
            return render(request,'selecBot.html')
    
    
def logBot(request):
    if len(request.GET) > 0:
        botId = request.GET.get('bot_id')
        request.session['logged_bot_id'] = botId
        return redirect('/dashboard')
    else:
        return render(request,'selectBot.html')
      
    
def dashboard(request):
    if 'logged_bot_id' in request.session:
        botId = request.session['logged_bot_id']
        bot = Bot.objects.get(pk=botId)
        return render(request, 'dashboard.html',
                    {'current_date_time':datetime.now,
                     'bot':bot,})
    else:
        return redirect('/selectBot')    
    
def config(request):
    if 'logged_bot_id' in request.session:
        botId = request.session['logged_bot_id']
        bot = Bot.objects.get(pk=botId)
        parts = Part.objects.filter(bot_id=botId)
        controlers = Controler.objects.all()
        servoTypes = ServoType.objects.all()
        speedClasses = SpeedClass.objects.all()
        sensorTypes = SensorType.objects.all()
        controlerTypes = ControlerType.objects.all()
        servos = Servo.objects.all()
        relays = Relay.objects.all()
        sensors = Sensor.objects.all()
              
        
        return render(request, 'config.html',
                    {'current_date_time':datetime.now,
                     'bot' : bot,
                     'parts' : parts,
                     'controlers' : controlers,
                     'servoTypes' : servoTypes,
                     'speedClasses' : speedClasses,
                     'sensorTypes' : sensorTypes,
                     'controlerTypes' : controlerTypes,
                     'servos' : servos,
                     'relays' : relays,
                     'sensors' : sensors,
                     
                     })
    else:
        return redirect('/selectBot')  