from django.shortcuts import render
from django.http import Http404

from .models import Room

def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})

def room_detail(request, room_id):
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        raise Http404('Room not found')
    return render(request, 'room_detail.html', {'room': room})