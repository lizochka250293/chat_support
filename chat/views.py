from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Number



def number(request, room_name):
    messages = Number.objects.filter(number=room_name)
    return render(request, 'chat/index.html', {"messages": messages, "room_name": room_name})


def room(request, room_name):
    return render(request,  'chat/room.html', context={"room_name": room_name})


def index(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        return redirect('index', room_name=number)
    return render(request, 'chat/number.html')
