from django.db import models
from civ.settings import MAKE_CHOICES, MODEL_CHOICES

# Create your models here.


class Civilian(models.Model):
    LICENSE_STATUS_CHOICES = (
        ('revoked', 'Revoked'),
        ('valid', 'Valid'),
        ('expired', 'expired'),
        ('none', 'None')
    )
    #name = models.
    driving_license = models.CharField(max_length=10, choices=LICENSE_STATUS_CHOICES, default=None)
    hunting_license = models.CharField(max_length=10, choices=LICENSE_STATUS_CHOICES, default=None)
    boating_license = models.CharField(max_length=10, choices=LICENSE_STATUS_CHOICES, default=None)
    weapon_permit = models.CharField(max_length=10, choices=LICENSE_STATUS_CHOICES, default=None)

class VehicleMake(models.Model):
    make = models.SmallIntegerField(choices=MAKE_CHOICES, default=58)

class VehicleModel(models.Model):
    make = models.ForeignKey(VehicleMake, related_name='vehiclemake', on_delete=models.CASCADE)
    model = models.CharField(max_length=40, choices=MODEL_CHOICES)

class Vehicle(models.Model):
    owner =  models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    #make_model = models.CharField(max_length=20, )
