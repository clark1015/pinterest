from django.shortcuts import render
from .models import *


# Create your views here.

def hello_world(request):

    if request.method == "POST":
        text = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = text
        new_hello_world.save()
        
        
        return render(request, 'accountapp/hello_world.html', {'text': new_hello_world.text})

    else:
        return render(request, 'accountapp/hello_world.html', {'text': 'GET METHOD!'})
    