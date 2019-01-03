
from django.shortcuts import render,redirect
from myBot.forms import BotAddForm
from myBot.models import Bot, Part

from datetime import datetime
    
def selectBot(request):
    bots = Bot.objects.all()
    return render(request, 'selectBot.html',
                  {'listBots':bots},
                  )

def logBot(request):
    if len(request.GET) > 0:
        botId = request.GET.get('bot_id')
        request.session['logged_bot_id'] = botId
        return redirect('dashboard/')
    else:
        return render(request,'selectBot.html')
    
def delBot(request):
    bots = Bot.objects.all()
    return render(request, 'delBot.html',
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

def dashboard(request):
    if 'logged_bot_id' in request.session:
        botId = request.session['logged_bot_id']
        bot = Bot.objects.get(pk=botId)
        return render(request, 'dashboard.html',
                    {'current_date_time':datetime.now,
                     'bot':bot,})
    else:
        return redirect('/selectBot')    