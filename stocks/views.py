from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home View</p>')

def room_detail(request, room_id):
    return HttpResponse(f'<h1>Room view with id {room_id}<h1>')