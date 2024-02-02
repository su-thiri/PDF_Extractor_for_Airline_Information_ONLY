from django.db import models

class UserImage(models.Model):
    image = models.ImageField(upload_to='user_images/')

class UserData(models.Model):
    booking_code = models.CharField(max_length=255,blank = True)
    eticket = models.CharField(max_length=255,blank = True)
    passenger_name = models.CharField(max_length=255,blank = True)
    passport_number = models.CharField(max_length=255,blank=True)
    travel_date = models.CharField(max_length=255,blank = True)
    desination = models.CharField(max_length=255,blank = True)
    departure_time = models.CharField(max_length=255,blank = True)
    arrival_time = models.CharField(max_length=255,blank = True)
    flight = models.CharField(max_length=255,blank = True)
    ar_class = models.CharField(max_length=255,blank = True)
    baggage_allowance = models.CharField(max_length=255,blank = True)
    issue_fare = models.CharField(max_length=255,blank = True)
    issue_date = models.CharField(max_length=255,blank = True)
    price = models.CharField(max_length=255,blank=True)

    