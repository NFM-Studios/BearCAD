from django.db import models

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
    MAKE_CHOICES = (
        ('albany', 'Albany'),
        ('annis', 'Annis'),
        ('benefactor', 'Benefactor'),
        ('bf', 'BF'),
        ('bollokan', 'Bollokan'),
        ('bravado', 'Bravado'),
        ('brute', 'Brute'),
        ('buckingham', 'Buckingham'),
        ('canis', 'Canis'),
        ('chariot', 'Chariot'),
        ('cheval', 'Cheval'),
        ('classique', 'Classique')
        ('coil', 'Coil'),
        ('desclasse', 'Desclasse'),
        ('dewbauchee', 'Dewbauchee'),
        ('dinka', 'Dinka'),
        ('dude', 'DUDE'),
        ('dundreary', 'Dundreary'),
        ('emperor', 'Emperor'),
        ('enus', 'Enus'),
        ('fathom', 'Fathom'),
        ('gallivanter', 'Gallivanter'),
        ('grotti', 'Grotti'),
        ('hvy', 'HVY'),
        ('hijack', 'Hijack'),
        ('imponte', 'Imponte'),
        ('invetero', 'Invetero'),
        ('jacksheepe', 'Jacksheepe'),
        ('jobuilt', 'JoBuilt'),
        ('karin', 'Karin'),
        ('kraken', 'Kraken'),
        ('lampadati', 'Lampadati'),

        #idk about this one
        ('liberty chop shop', 'liberty Chop Shop'),

        ('liberty city cycles', 'Liberty City Cycles'),
        ('maibatsu corporation', 'Maibatsu Corporation'),
        ('mammoth', 'Mammoth'),
        ('mtl', 'MTL'),
        ('nagasaki', 'Nagasaki'),
        ('obey', 'Obey'),
        ('ocelot', 'Ocelot'),
        ('overflod', 'Overflod'),
        ('pegassi', 'Pegassi'),
        ('pfister', 'Pfister'),
        ('principle', 'Principle'),
        ('progen', 'Progen'),
        ('schyster', 'Schyster'),
        ('shitzu', 'Shitzu'),
        ('speedophile', 'Speedophile'),
        ('stanley', 'Stanley'),
        ('steel horse', 'Steel Horse')
        ('tuffade', 'Tuffade'),
        ('ubermacht', 'Ubermacht'),
        ('vapid', 'Vapid'),
        ('vulcar', 'Vulcar'),
        ('weeny', 'Weeny'),
        ('western company' , 'Western Company'),
        ('western motorcyle company', 'Western Motorcyle Company'),
        ('willard', 'Willard'),
        ('zirconium', 'Zirconium'),
        ('none', 'None')
    )
    make = models.CharField(max_length=40, choices=MAKE_CHOICES, default=None)

class VehicleModel(models.Model):
    MODEL_CHOICES = (
        #albany
        ('alpha', 'Alpha'),
        ('buccaneer', 'Buccaneer'),
        ('buccaneer custom', 'Buccaneer Custom'),
        ('cavalcade', 'Cavalcade'),
        ('cavalcade fxt', 'Cavalcade FXT')
        ('emperor', 'Emperor'),
        ('esperanto', 'Esperatno'),
        ('fanken stange', 'Fanken Stange'),
        

    )
    make = models.ForeignKey(VehicleMake, related_name='vehiclemake', on_delete=models.CASCADE)
    model = models.CharField(max_length=40, choices=MODEL_CHOICES)

class Vehicle(models.Model):
    owner =  models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    #make_model = models.CharField(max_length=20, )
