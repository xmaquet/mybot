from django.contrib import admin
from myBot.models import *

class ControlerAdmin(admin.TabularInline):
    model = Controler

class PartAdmin(admin.TabularInline):
    model = Part
    
class ServoAdmin(admin.TabularInline):
    model = Servo
    
class SensorAdmin(admin.TabularInline):
    model = Sensor
    
class RelayAdmin(admin.TabularInline):
    model = Relay

class DeviceInControler(admin.ModelAdmin):
    list_display = ('title','code')
    inlines = [ServoAdmin,SensorAdmin,RelayAdmin]
    
class PartinBot(admin.ModelAdmin):
    list_display = ('title','bot')
    inlines = [ControlerAdmin]
    
class BotAdmin(admin.ModelAdmin):
    model = Bot
    inlines = [PartAdmin,]
    list_display = ('botModel','botName','botOwner','localization')
    
    
admin.site.register(Bot, BotAdmin)
admin.site.register(Part, PartinBot)
admin.site.register(Controler,DeviceInControler)
admin.site.register(Device)
admin.site.register(Servo)
admin.site.register(ServoType)
admin.site.register(SpeedClass)
admin.site.register(Sensor)
admin.site.register(SensorType)
admin.site.register(Relay)
admin.site.register(PowerLine)
admin.site.register(Function)
admin.site.register(Service)
admin.site.register(ControlerType)
admin.site.register(Serial)
admin.site.register(TcpIp)
admin.site.register(Action)

