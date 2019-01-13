
from django.shortcuts import render,redirect, get_object_or_404
from myBot.forms import BotAddForm,PartAddForm,ControlerAddForm,ServoAddForm,RelayAddForm,SensorAddForm
from myBot.models import Bot, Part, Controler,ControlerType, ServoType, SpeedClass, SensorType, Servo, Relay, Sensor
from datetime import datetime
    
def selectBot(request):
    bots = Bot.objects.all()
    if 'logged_bot_id' in request.session:
        botId = request.session['logged_bot_id']
        bot = Bot.objects.get(pk=botId)
    return render(request, 'selectBot.html',
                  {'listBots':bots,
                   'bot':bot},
                  )

def logBot(request):
    if len(request.GET) > 0:
        botId = request.GET.get('bot_id')
        request.session['logged_bot_id'] = botId
        return redirect('/dashboard')
    else:
        return render(request,'selectBot.html')
    
def delBot(request):
    bots = Bot.objects.all()
    return render(request, 'delBot.html',
                  {'listBots':bots},
                  )
    
def editBot(request):
    bots = Bot.objects.all()
    return render(request, 'editBot.html',
                  {'listBots':bots},
                  )
    
def addBot(request):
    if len(request.GET) > 0:
        form = BotAddForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/selectBot')
        else:
            return render(request,'addBot.html', {'form':form})
    else:
        form = BotAddForm()
        return render(request, 'addBot.html', {'form':form})
    
def addPart(request):
    if 'logged_bot_id' in request.session:
        botId = request.session['logged_bot_id']
        bot = Bot.objects.get(pk=botId)
        form = PartAddForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/config')
        else:
            return render(request,'structure/addPart.html', {'form':form,
                                                             'bot' : bot,})
    else:
        form = PartAddForm()
        return render(request, 'structure/addPart.html', {'form':form,
                                                          'bot' : bot,})

def addControler(request):
    if 'logged_bot_id' in request.session:
        botId = request.session['logged_bot_id']
        bot = Bot.objects.get(pk=botId)
        form = ControlerAddForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/config')
        else:
            return render(request,'structure/addControler.html', {'form':form,
                                                                  'bot' : bot})
    else:
        form = ControlerAddForm()
        return render(request, 'structure/addControler.html', {'form':form,
                                                               'bot' : bot})
    
def addServo(request):
    if len(request.GET) > 0:
        form = ServoAddForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/config')
        else:
            return render(request,'structure/addServo.html', {'form':form})
    else:
        form = ServoAddForm()
        return render(request, 'structure/addServo.html', {'form':form})

    
def addRelay(request):
    if len(request.GET) > 0:
        form = RelayAddForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/config')
        else:
            return render(request,'structure/addRelay.html', {'form':form})
    else:
        form = RelayAddForm()
        return render(request, 'structure/addRelay.html', {'form':form})
    
def addSensor(request):
    if len(request.GET) > 0:
        form = SensorAddForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/config')
        else:
            return render(request,'structure/addSensor.html', {'form':form})
    else:
        form = SensorAddForm()
        return render(request, 'structure/addSensor.html', {'form':form})
    
    
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