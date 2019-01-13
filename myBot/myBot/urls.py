"""myBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myBot.views import dashboard,selectBot,addBot,delBot,editBot,logBot,config,addPart,addControler,addServo,addRelay,addSensor

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', selectBot),
    url('^dashboard$', dashboard),
    url('^selectBot$', selectBot),
    url('^addBot$', addBot),
    url('^delBot$', delBot),
    url('^editBot$', editBot),
    url('^logBot$',logBot),
    url('^config$',config),
    url('^addPart$',addPart),
    url('^addControler$',addControler),
    url('^addServo$',addServo),
    url('^addRelay$',addRelay),
    url('^addSensor$',addSensor),
]
