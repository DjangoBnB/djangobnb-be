from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=50)
    room_des = models.TextField()
    
    room_address_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    room_address_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # room_image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    room_max = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RoomCategory(models.Model):
    pass

class Review(models.Model):
    pass

class RoomOption(models.Model):
    pass

class RoomReservation(models.Model):
    pass

