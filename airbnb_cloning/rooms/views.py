from django.shortcuts import render
from .models import Room, Review, Book
from .serializers import RoomListSerializer, RoomSerializer, ReviewSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET',])
def index(request):
    rooms = Room.objects.all()
    room_option = request.GET.getlist('option')
    room_type = request.GET.get('type')
    place = request.GET.getlist('place')
    count_p = request.GET.get('count_p')
    filtered_rooms = rooms

    if room_type:
        filtered_rooms = filtered_rooms.filter(room_type=room_type)

    if room_option:
        for option in room_option:
            filtered_rooms = filtered_rooms.filter(room_option__id__in=option)

    if place:
        for p in place:
            filtered_rooms = filtered_rooms.filter(room_address__contains=p)

    if count_p:
        filtered_rooms = filtered_rooms.filter(room_max__gte=count_p)
    # 이상: __gte, 초과: __gt, 이하:__lte, 미만:__lt
    
    serializer = RoomListSerializer(filtered_rooms, many=True)
    return Response(serializer.data)


@api_view(['GET',])
def detail(request, room_id):
    room = Room.objects.get(id=room_id)
    serializer = RoomSerializer(room)
    return Response(serializer.data)


@api_view(['GET',])
def reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)



@api_view(['POST',])
@permission_classes([IsAuthenticated])
def book(request, room_id):
    # print(requests.data)
    room = Room.objects.get(id=room_id)
    serializer = BookSerializer(data=request.data)
    print(request.user)
    if serializer.is_valid():
        print(request.user)
        serializer.save(book_user=request.user, book_room=room)
        return Response(serializer.data)
    print(serializer.errors)
