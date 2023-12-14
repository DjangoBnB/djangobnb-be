from django.shortcuts import render
from .models import Room, Review, Book
from .serializers import RoomListSerializer, RoomSerializer, ReviewSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET',])
def index(requests):
    rooms = Room.objects.all()
    serializer = RoomListSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET',])
def detail(requests, room_id):
    room = Room.objects.get(id=room_id)
    serializer = RoomSerializer(room)
    return Response(serializer.data)


@api_view(['GET',])
def reviews(requests):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)



@api_view(['POST',])
@permission_classes([IsAuthenticated])
def book(requests, room_id):
    # print(requests.data)
    room = Room.objects.get(id=room_id)
    serializer = BookSerializer(data=requests.data)
    print(requests.user)
    if serializer.is_valid():
        print(requests.user)
        serializer.save(book_user=requests.user, book_room=room)
        return Response(serializer.data)
    print(serializer.errors)
