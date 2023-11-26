from django.shortcuts import render
from .models import Room
from django.response import Response

# Create your views here.
def index(requests):
    rooms = Room.objects.all()
    serializer = Room