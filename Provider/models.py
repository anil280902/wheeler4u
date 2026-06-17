from django.contrib.auth.models import User
from django.db import models
from User.models import user


# Create your models here.
class provider(models.Model):
    p= models.OneToOneField(User, on_delete=models.CASCADE)
    Provider_name = models.CharField(max_length=80)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    Phone_no = models.CharField(max_length=13)
    Business_name = models.CharField(max_length=80)
    GST_id = models.CharField(max_length=15)
    Business_address = models.CharField(max_length=300)
    Earnings = models.IntegerField(default=0)

    def __str__(self):
        return self.Provider_name

class Vehicle(models.Model):
    Provider_id = models.ForeignKey(provider, on_delete=models.CASCADE)
    Brand_name = models.CharField(max_length=60)
    Vehicle_model = models.CharField(max_length=50)
    Vehicle_number = models.CharField(max_length=10)
    Chassis_no = models.CharField(max_length=17)
    Fuel_type = models.CharField(max_length=20)
    Transmission_type = models.CharField(max_length=20)
    Seating_capacity = models.IntegerField()
    Rent_price = models.IntegerField()
    Vehicle_img1 = models.ImageField()
    Img_insurance = models.ImageField()

    def __str__(self):
        return self.Vehicle_number

class Payment_provider(models.Model):
    Provider_id = models.ForeignKey(provider, on_delete=models.CASCADE)
    Vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Amount = models.IntegerField()
    Admin_commission = models.IntegerField()
    Pay_date_time = models.DateTimeField()
    Invoice_no = models.CharField(max_length=10)