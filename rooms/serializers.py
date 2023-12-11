from rest_framework import serializers
from .models import Room, Review, Type, Option, Book, Room_image
from django.db.models import Avg


class ReviewSerializer(serializers.ModelSerializer):
    review_author = serializers.CharField(source='review_author.nickname', read_only=True)

    class Meta():
        model = Review
        fields = ['review_author', 'review_score', 'review_content', 'review_created_at', 'review_updated_at',]


class TypeSerializer(serializers.ModelSerializer):
    class Meta():
        model = Type
        fields = ['name',]


class OptionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Option
        fields = ['name',]


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta():
        model = Room_image
        fields = ['image_url',]


class RoomListSerializer(serializers.ModelSerializer):
    room_score = serializers.SerializerMethodField()
    room_reviews_count = serializers.IntegerField(source='room_reviewed.count', read_only=True)
    room_host = serializers.CharField(source='room_host_name.name', read_only=True)
    room_images = serializers.CharField(source='room_images.image_url', read_only=True)

    class Meta():
        model = Room
        exclude = ['room_lat', 'room_long', 'room_des', 'room_reviews']
    
    def get_room_score(self, obj):
        av = Review.objects.filter(review_room=obj.id).aggregate(Avg('review_score')).get('review_score__avg')

        if av is None:
            return 0
        return round(av, 1)


class BookSerializer(serializers.ModelSerializer):
    class Meta():
        model = Book
        fields = '__all__'
        read_only_fields = ('book_user', 'book_room',)



class RoomSerializer(serializers.ModelSerializer):
    class BookSerializer(serializers.ModelSerializer):
        class Meta():
            model = Book
            fields = ['book_check_in', 'book_check_out']
    # serializer의 SerializerMethodField를 이용하여 rate의 평균값을 구한다
    room_score = serializers.SerializerMethodField()
    room_reviews_count = serializers.IntegerField(source='room_reviewed.count', read_only=True)
    room_host_name = serializers.CharField(source='room_host_name.name', read_only=True)
    room_type = serializers.CharField(source='room_type.name', read_only=True)
    room_option = OptionSerializer(many=True, read_only=True)
    room_reviews = ReviewSerializer(source='room_reviewed', many=True, read_only=True)
    room_booked = BookSerializer(source='booked_room', many=True, read_only=True)
    room_images = RoomImageSerializer(many=True, read_only=True)


    class Meta():
        model = Room
        fields = '__all__'
    
    def get_room_score(self, obj):
        av = Review.objects.filter(review_room=obj.id).aggregate(Avg('review_score')).get('review_score__avg')

        if av is None:
            return 0
        return round(av, 1)
     

