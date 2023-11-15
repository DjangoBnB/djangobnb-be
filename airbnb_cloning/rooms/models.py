from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=50)
    room_address_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    room_address_longitude = models.DecimalField(max_digits=9, decimal_places=6)    
    room_des = models.TextField()    
    # room_image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    room_country = models.CharField(max_length=50, default="한국")
    room_city = models.CharField(max_length=50, default="서울")
    room_max = models.PositiveIntegerField()
    room_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # room_option = models.ManyToManyField()
    # room_category = models.ManyToManyField()
    # review = models.ManyToManyField(get_user_model(), through='Review', related_name='room_review' )


class RoomCategory(models.Model):
    category_name = models.CharField(max_length=10)
    category_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    


class RoomOption(models.Model):
    option_name = models.CharField(max_length=10)
    option_room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Review(models.Model):
    room_review = models.ForeignKey(Room, on_delete=models.CASCADE) 
    review_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review_content = models.TextField()
    # review_score = ''
    # review_image = ''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Host(models.Model):
    host_name = models.CharField(max_length=20)
    host_room = models.ForeignKey(Room)
    # host_room은 cascade할 이유가 있는가

class RoomReservation(models.Model):
    pass

