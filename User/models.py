from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class user(models.Model):
    u=models.OneToOneField(User,on_delete=models.CASCADE)
    User_name = models.CharField(max_length=80)
    Gender = models.CharField(max_length=6)
    Address = models.CharField(max_length=300)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    Phone_no = models.CharField(max_length=13)
    Licence_no = models.CharField(max_length=15)
    Deposit = models.IntegerField()

    def __str__(self):
        return self.User_name