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
        )
    controlerType = models.ForeignKey(
        'ControlerType',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='type de contrôleur',
        )
    interface = models.ForeignKey(
        'Interface',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='type d\'interface',
        )
    def __str__(self):
        return self.title
    
class Interface(models.Model):
    title = models.CharField(
        max_length=50,
        null=False,
        default='undefined',
        verbose_name = "intitulé",
        )
    code = models.CharField(
        max_length=20,
        null=True,
        )
    link = models.ForeignKey(
        'Link',
        on_delete=models.CASCADE,
        null=True,
        )
    def __str__(self):
        return self.title
    
class Link(models.Model):
    type = models.CharField(
        max_length=50,
        null=False,
        default='undefined',
        )
    def __str__(self):
        return self.type
    
class ControlerType(models.Model):
    brand = models.CharField(
        max_length=20,)
    model = models.CharField(
        max_length=20,)
    maxDigitalPins = models.PositiveIntegerField()
    maxAnalogPins = models.PositiveIntegerField()
    def __str__(self):
        return self.brand +" "+self.model
    
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
        blank=True,)
    prefix = models.CharField(
        max_length=10,
        null=True,
        blank=False,
        default='undefined',
        help_text="utilisé dans l\'adressage du device")
    index = models.PositiveIntegerField(
        null=True,
        help_text="combiné au préfixe pour adressage")
    def __str__(self):
        return self.title
    
class Servo(Device):
    rev = models.BooleanField()
    toggle = models.BooleanField()
    min = models.PositiveIntegerField(
        null=False,
        default=0,)
    max = models.PositiveIntegerField(
        null=False,
        default=180,)
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
    
class SpeedClass(models.Model):
    timeInSec = models.PositiveIntegerField()
    rotInDeg = models.PositiveIntegerField()
        
class Sensor(Device):
    mesureUnit = models.CharField(
        max_length=20
        )

class Relay(Device):
    levelList = (
        ('Low','Niveau bas'),
        ('High','Niveau haut'),
        )
    closeLevel = models.CharField(
        max_length=5,
        choices = levelList,
        default='Low',
        )
    
class PowerLine(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name = "intitulé",
        )
    code = models.CharField(
        max_length=20
        )
    def __str__(self):
        return self.title
    
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
    