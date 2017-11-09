"""iotdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views as thing

urlpatterns = [
    url(r'^$', view=thing.index, name="index"),
    url(r'^thing/register$', view=thing.thingRegister, name="register"),
    url(r'^things$', view=thing.things, name="things"),
    url(r'^thing/(?P<id>[A-Za-z0-9]+)$', view=thing.readStatus, name="read"),
    url(r'^thing/(?P<id>[A-Za-z0-9]+)/(?P<status>[A-Za-z0-9,\[\].]+)$', view=thing.writeStatus, name="write"),

]
