from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from api.models import Things


def readStatus(request, id):
    thing = Things.objects.filter(id=id)
    if len(thing) == 0:
        return HttpResponse("No such thing exists")
    thing = thing[0]
    status = thing.status
    return HttpResponse("{}".format(status))


def writeStatus(request, id, status):
    thing = Things.objects.filter(id=id)
    if len(thing) == 0:
        return HttpResponse("No such thing exists")
    thing = thing[0]
    thing.status = status
    thing.save(force_update=True)
    return HttpResponse("Woah I need to write this status -- {} ".format(status))


def thingRegister(request):
    if request.method == "GET":

        return render(request, 'api/register.html')
    elif request.method == "POST":
        thingname = request.POST["thingname"]
        thingid = request.POST["thingname"]
        t = Things(name=thingname, id=thingid, status='0')
        t.save()
        return render(request, 'api/register.html', {"message": "Registration successful"})


def index(request):
    return render(request, 'api/index.html')


def things(request):
    things = list(Things.objects.all())

    return render(request, 'api/things.html', {"things": things})
