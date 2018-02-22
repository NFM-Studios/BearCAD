from django.db import models

# Create your models here.


class Civilian(models.Model):
    LICENSE_STATUS_CHOICES = (
        ('revoked', 'Revoked'),
        ('valid', 'Valid'),
        ('expired', 'expired'),
        ('none', 'None')
    )
    name = models.
    driving_license = models.CharField(max_length=10, choices=LICENSE_STATUS_CHOICES, default=none)
    hunting_license = models.CharField(max_length=10, choices=LICENSE_STATUS_CHOICES, default=none)
    boating_license = models.CharField(max_length=10, choices=LICENSE_STATUS_CHOICES, default=none)
    weapon_permit = models.CharField(max_length=10, choices=LICENSE_STATUS_CHOICES, default=none)


class Vehicle(models.Model):
    MAKE_MODEL_CHOICES = (
        ('albany')
    )
    make_model = models.CharField(max_length=20, )
