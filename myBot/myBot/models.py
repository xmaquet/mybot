# -*- coding: utf-8 -*-
from django.db import models


class Bot(models.Model):
    botModel = models.CharField(
        max_length=50,
        verbose_name = "modèle",
        )
    botName = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name = "nom",
        )
    botOwner = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name = "propriétaire",
        )
    locList =(
        ('loc','Local'),
        ('rem','Remote'),
        )
    localization = models.CharField(
        max_length=20,
        choices = locList,
        default='Loc',
        verbose_name = "localisation",
        help_text="Local : le Bot est sur la même machine que le système "
        )
    image = models.ImageField(
        max_length=255,
        blank=True,
        null=True,)
    
    reg_date = models.DateField(
        auto_now_add=True,
        )
    
    def __str__(self):
        return self.botModel
    
class Part(models.Model):
    bot = models.ForeignKey(
        'Bot',
        on_delete=models.CASCADE,
        verbose_name = "bot",)
    title = models.CharField(
        max_length=50,
        verbose_name = "intitulé",
        )
    def __str__(self):
        return self.title
    def key(self):
        key = "part" + str(self.id) 
        return key
    
class Controler(models.Model):
    part = models.ForeignKey(
        'Part',
        on_delete=models.CASCADE,
        verbose_name='A quelle partie appartient ce contrôleur ?'
        )
    title = models.CharField(
        max_length=50,
        verbose_name = "intitulé",
        )
    code = models.CharField(
        max_length=20
        )
    address = models.CharField(
        max_length=50,
        null=True,
        blank=False,
        verbose_name = "adresse",
        help_text = 'paste or select',
        )
    controlerType = models.ForeignKey(
        'ControlerType',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='type de contrôleur',
        )
    typeList = (
        ('usb','USB-Serial'),
        ('ip-eth','IP on Ethernet'),
        ('ip-wifi','IP on Wifi'),
        )
    interface = models.CharField(
        max_length=10,
        choices=typeList,
        default='usb',
        verbose_name='type d\'interface',
        )
    def __str__(self):
        return self.title   

    def key(self):
        key = "controler" + str(self.id) 
        return key
    
class ControlerType(models.Model):
    brand = models.CharField(
        max_length=20,)
    model = models.CharField(
        max_length=20,)
    maxDigitalPins = models.PositiveIntegerField()
    maxAnalogPins = models.PositiveIntegerField()
    def __str__(self):
        return self.brand +" "+self.model
    def key(self):
        key = "controlerType" + str(self.id) 
        return key
    
class Device(models.Model):
    controler = models.ForeignKey(
        'Controler',
        on_delete=models.CASCADE,)
    title = models.CharField(
        max_length=50,
        verbose_name = "intitulé",
        )
    code = models.CharField(
        max_length=20
        )
    pinNum = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='n° de broche',
        help_text='donné à titre indicatif',)
    prefix = models.CharField(
        max_length=10,
        null=True,
        blank=False,
        help_text="utilisé dans l\'adressage du device",
        verbose_name='préfixe pour l\'adressage',)
    index = models.PositiveIntegerField(
        null=True,
        help_text="combiné au préfixe pour adressage")
    def __str__(self):
        return self.title
    def key(self):
        key = "device" + str(self.id) 
        return key
    
class Servo(Device):
    model = models.CharField(
        max_length=20,
        blank=False,
        verbose_name = 'marque ou modèle (ou standard)',)
    rev = models.BooleanField()
    toggle = models.BooleanField()
    min = models.PositiveIntegerField(
        null=False,
        default=0,
        verbose_name='valeur minimale',
        help_text = 'en action, le servo ne pourra pas aller sous cette valeur')
    max = models.PositiveIntegerField(
        null=False,
        default=180,
        verbose_name='valeur maximale',
        help_text = 'en action, le servo ne pourra pas aller au-dessus de cette valeur')
    servoType = models.ForeignKey(
        'ServoType',
        on_delete=models.CASCADE,
        null=True,
        )
    speedClass = models.ForeignKey(
        'SpeedClass',
        on_delete=models.CASCADE,
        null=True,
        )

class ServoType(models.Model):
    typeList = (
        ('lin','Linéaire'),
        ('ang','Angulaire'),
        )
    type = models.CharField(
        max_length=3,
        choices=typeList,
        default='ang',) 
    def __str__(self):
        return self.type
    def key(self):
        key = "servoType" + str(self.id) 
        return key
    
class SpeedClass(models.Model):
    timeInSec = models.PositiveIntegerField()
    rotInDeg = models.PositiveIntegerField()
    def key(self):
        key = "speedClass" + str(self.id) 
        return key
        
class Sensor(Device):
    mesureUnit = models.CharField(
        max_length=20,
        blank = False,
        null = True,
        verbose_name='unité de mesure'
        )
    def key(self):
        key = "sensor" + str(self.id) 
        return key
    
class SensorType(models.Model):
    title = models.CharField(
        max_length = 50,
        blank = False,
        null = True,)
    def key(self):
        key = "sensorType" + str(self.id) 
        return key

class Relay(Device):
    levelList = (
        ('Low','Niveau bas'),
        ('High','Niveau haut'),
        )
    closeLevel = models.CharField(
        max_length=5,
        choices = levelList,
        default='Low',
        verbose_name='niveau fermé',
        help_text='précise le niveau à donner à la broche pour fermer le relais'
        )
    def key(self):
        key = "relay" + str(self.id) 
        return key
    
class PowerLine(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name = "intitulé",
        )
    code = models.CharField(
        max_length=20
        )
    maxCurrent = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        help_text='unité = A',
         verbose_name='courant maximal prévu',
         null=True,
         blank=False,
         default=0,)
       
        
    def __str__(self):
        return self.title
    
    def key(self):
        key = "powerLine" + str(self.id) 
        return key
    
class Function(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name = "intitulé",
        )
    code = models.CharField(
        max_length=20
        )
    part = models.ForeignKey(
        'Part',
        on_delete=models.CASCADE,
        null=True,
        )
    def __str__(self):
        return self.title
    def key(self):
        key = "function" + str(self.id) 
        return key
    
class Service(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name = "intitulé",
        )
    code = models.CharField(
        max_length=20,
        null=True,
        default='service',
        )
    def __str__(self):
        return self.title
    def key(self):
        key = "service" + str(self.id) 
        return key
    