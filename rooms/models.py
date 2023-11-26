from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=50)
    room_address_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    room_address_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    room_image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    room_des = models.TextField()
    room_capacity = models.IntegerField()
    room_reservation = models.ManyToManyField(get_user_model(), through='Reservation', related_name='user_room')
    room_review = models.ManyToManyField(get_user_model(), through='Review', related_name='review_room')
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

class Category(models.Model):
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Host(models.Model):
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)









