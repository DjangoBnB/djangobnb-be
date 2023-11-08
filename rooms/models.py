from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    image = models.TextField()
    description = models.TextField()
    capacity = models.IntegerField()
    # reservation = models.ManyToManyField(get_user_model(), through='Reservation', related_name='reserv_room')
    review = models.ManyToManyField(get_user_model(), through='Review', related_name='review_room')

# class Reservation(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     check_in = models.DateField()
#     check_out = models.DateField()

class Review(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reviewed_room')
    rating = models.FloatField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Host(models.Model):
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)









