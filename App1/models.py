from datetime import datetime
from django.db import models
from Provider.models import provider,Vehicle
from User.models import user
from django.contrib.auth.models import User


# Create your models here.

class Admin_earnings(models.Model):
    A_earnings = models.IntegerField()

class Category(models.Model):
    Category_name = models.CharField(max_length=10)

    def __str__(self):
        return self.Category_name

class Subcategory(models.Model):
    Subcategory = models.CharField(max_length=100)
    Cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.Subcategory

class Payment(models.Model):
    User_id = models.ForeignKey(user, on_delete=models.CASCADE)
    Vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Amount = models.IntegerField()
    Pay_date_time = models.DateTimeField()
    Invoice_no = models.CharField(max_length=10)


class Booking(models.Model):
    User_id = models.ForeignKey(user, on_delete=models.CASCADE)
    Provider_id = models.ForeignKey(provider, on_delete=models.CASCADE)
    Vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    B_start_date = models.DateTimeField()
    B_end_date = models.DateTimeField()
    Created_at = models.DateField()
    Starting_location = models.CharField(max_length=300)
    Ending_location = models.CharField(max_length=300)


class Feedback(models.Model):
    Booking_id = models.IntegerField()
    User_id = models.IntegerField()
    Provider_id = models.IntegerField()
    Message = models.CharField(max_length=300)

