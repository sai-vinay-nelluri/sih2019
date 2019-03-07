from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Sale(models.Model):
    vehicles = [('xl-50', 'xl-50'), ('jupiter', 'jupiter'), ('apache', 'apache'), ('pep', 'pep')]
    colors = [('red', 'red'), ('green', 'green'), ('silver', 'silver'), ('blue', 'blue'), ('black', 'black'), ('white', 'white')]

    d = {
        'scooters': ['ntorq', 'jupiter', 'wego', 'zest', 'pep+'],
        'motorcycles': ['victor', 'sport', 'radeon', 'star city+', 'apache rtr 160 4v', 'apache rtr 200 4v', 'apache rr310'],
        'moped': ['xl100', ],
        'three_wheelers': ['king', ]
    }
    name = models.CharField(max_length=64, blank=False)
    mobile_number = models.CharField(max_length=10, blank=False)
    location = models.CharField(max_length=64, blank=False)
    location_type = models.CharField(max_length=10,blank=False)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=6, blank=False)
    vehicle_type = models.CharField(max_length=64)
    vehicle_name = models.CharField(max_length=32)
    vehicle_color = models.CharField(max_length=32, choices=colors)
    date = models.DateTimeField(default=timezone.now)
    mode_known = models.CharField(max_length=64, blank=False, default="other")


class ShowRoom(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sales = models.ManyToManyField(to=Sale)
