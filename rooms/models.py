from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Host(models.Model):
    name = models.CharField(max_length=20)


class Category(models.Model):
    name = models.CharField(max_length=20)


class Room(models.Model):
    room_name = models.CharField(max_length=50)
    room_address_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    room_address_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    room_address = models.CharField(max_length=50)
    room_des = models.TextField()
    room_capacity = models.IntegerField()
    room_types = models.ManyToManyField(Category, blank=True, through='Room_Category', related_name='types_room')
    room_reservation = models.ManyToManyField(get_user_model(), null=True, through='Reservation', related_name='user_room')
    room_review = models.ManyToManyField(get_user_model(), null=True, through='Review', related_name='review_room')
    room_host = models.ForeignKey(Host, on_delete=models.CASCADE)
    room_daily_price = models.IntegerField()
    room_created_at = models.DateTimeField(auto_now_add=True)
    room_updated_at = models.DateTimeField(auto_now=True)

class Reservation(models.Model):
    reservation_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_reservated')
    reservation_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_reservated')
    reservation_check_in = models.DateField()
    reservation_check_out = models.DateField()

class Review(models.Model):
    review_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_reviewed')
    review_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_reviewed')
    review_rating = models.FloatField()
    review_comment = models.TextField()
    review_created_at = models.DateTimeField(auto_now_add=True)
    review_updated_at = models.DateTimeField(auto_now=True)

class Room_Category(models.Model):
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)



class Room_image(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    image_url = models.ImageField(blank=True, upload_to='%Y/%m/%d/')






