from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def hello_world(request):

    if request.method == "POST":
        text = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = text
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    