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
    image = models.ImageField(
        blank=True,
        null=True,)
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
        on_delete=models.CASCADE,
        verbose_name='contrôleur de rattachement')
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

    rev = models.BooleanField(
        verbose_name='reverse',
        help_text='inverser le sens de fonctionnement')
    toggle = models.BooleanField(
        verbose_name='trigger',
        help_text='le servo se comporte comme un interrupteur')
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
        verbose_name='type de servo',
        )


class ServoType(models.Model):
    typeList = (
        ('lin','Linéaire'),
        ('ang','Angulaire'),
        )
    model = models.CharField(
        max_length=20,
        blank=False,
        verbose_name = 'marque ou modèle (ou standard)',
        null=True,)
    type = models.CharField(
        max_length=3,
        choices=typeList,
        default='ang',) 
    speedClass = models.ForeignKey(
        'SpeedClass',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='classe de vitesse',
        help_text='la classe de vitesse est indispensable pour moduler la vitesse du servo'
        )
    def __str__(self):
        return self.model
    def key(self):
        key = "servoType" + str(self.id) 
        return key
    
class SpeedClass(models.Model):
    title = models.CharField(
        max_length = 50,
        blank = False,
        null = True,)
    timeInSec = models.PositiveIntegerField(
        verbose_name='temps en secondes',)
    move = models.PositiveIntegerField(
        verbose_name='valeur du mouvement',
        null = True)
    unit = models.CharField(
        max_length = 20,
        blank = False,
        null = True,
        verbose_name = 'unité de mouvement')
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

class Interface(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='intitulé',
        ) 
    def __str__(self):
        return self.title
    
class Serial(Interface):
    baudrateList = (
        ('9600','9600'),
        ('19200','19200'),
        ('57600','57600'),
        ('115200','115200'),)
    bytesizeList = (
        ('FIVEBITS','5'),
        ('SIXBITS','6'),
        ('SEVENBITS','7'),
        ('EIGHTBITS','8'),)
    parityList = (
        ('PARITY_NONE','None'),
        ('PARITY_EVEN','Even'),
        ('PARITY_ODD','Odd'),
        ('PARITY_MARK','Mark'),
        ('PARITY_SPACE','Space'),)
    stopbitsList =(
        ('STOPBITS_ONE','1'),
        ('STOPBITS_ONE_POINT_FIVE','1,5'),
        ('STOPBITS_TWO','2'),)
    port = models.CharField(
        max_length = 100,
        verbose_name = 'nom de l\'interface',
        help_text ='depending on operating system. e.g. /dev/ttyUSB0 on GNU/Linux or COM3 on Windows.',
        null=False,
        blank = False,
        )
    baudrate = models.CharField(
        max_length=10,
        choices = baudrateList,
        null = False,
        blank = False,
        default = '115200',
        verbose_name='débit (baudrate)'
        )
    bytesize = models.CharField(
        max_length=100,
        choices = bytesizeList,
        null = False,
        blank = False,
        default = '8',
        verbose_name = 'octets de données (bytesize)')
    parity = models.CharField(
        max_length = 100,
        choices = parityList,
        null = False,
        blank = False,
        default = 'None')
    stopbits = models.CharField(
        max_length = 20,
        choices = stopbitsList,
        null = False,
        blank = False,
        default = '1',
        verbose_name = 'bits de stop')
    timeout = models.CharField(
        max_length = 20,
        null = False,
        blank = False,
        default = 'None',
        verbose_name = 'timeout = 0: non-blocking mode, return immediately in any case, returning zero or more, up to the requested number of bytes',
        help_text = 'Set a read timeout value.'),
    xonxoff = models.BooleanField(
        default = False,
        verbose_name = 'xonxoff : Enable software flow control',)
    rtscts = models.BooleanField(
        default = False,
        verbose_name = 'Enable hardware (RTS/CTS) flow control.',)
    dsrdtr = models.BooleanField(
        default = False,
        verbose_name = 'Enable hardware (DSR/DTR) flow control.',)
    write_timeout = models.CharField(
        max_length = 20,
        null = False,
        blank = False,
        help_text = 'Set a write timeout value',
        default='None',)
    inter_byte_timeout = models.CharField(
        max_length = 20,
        null = False,
        blank = False,
        help_text = 'Inter-character timeout, None to disable (default).',
        default='None',)
    exclusive = models.CharField(
        max_length = 20,
        null = False,
        blank = False,
        default = 'None',
        help_text = ' Set exclusive access mode (POSIX only). A port cannot be opened in exclusive access mode if it is already open in exclusive access mode.',
        )