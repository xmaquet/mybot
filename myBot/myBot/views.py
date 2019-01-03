
from django.shortcuts import render,redirect
from myBot.forms import BotAddForm
from myBot.models import Bot, Part

from datetime import datetime
    
def selectBot(request):
    bots = Bot.objects.all()
    return render(request, 'selectBot.html',
                  {'listBots':bots},
                  )
    
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
    botId = request.GET.get('bot_id')
    bot = Bot.objects.get(pk=botId)
    parts = Part.objects.get(bot_id=botId)
    return render(request, 'dashboard.html',
                    {'current_date_time':datetime.now,
                    'bot_name':bot.botName,
                    'bot_owner':bot.botOwner,
                    'bot_model':bot.botModel,
                    'listParts':parts,}
                                      )    