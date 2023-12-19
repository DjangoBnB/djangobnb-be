from django.shortcuts import render
from .models import Room, Review, Book
from .serializers import RoomListSerializer, RoomSerializer, ReviewSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET',])
def index(request):
    rooms = Room.objects.all()
    serializer = RoomListSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST',])
def detail(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'GET':
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = BookSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save(book_user=request.user, book_room=room)
                return Response(serializer.data)
    


@api_view(['GET',])
def reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

    

@api_view(['GET',])
def book_list(request, user_id):
    user = get_user_model().objects.get(id=user_id)
    books = Book.objects.filter(book_user=user)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'DELETE':
        book.delete()
        return Response({"message": "Book deleted successfully."})
    

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def likes(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.user in room.room_like_users.all():
        room.room_like_users.remove(request.user)
        is_like = False
    else:
        room.room_like_users.add(request.user)
        is_like = True

    # serializer = ArticleSerializer(article)
    return Response({'is_like': is_like})