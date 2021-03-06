from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    def __str__(self):
        return str(self.user)
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    #email_verified = models.BooleanField(default=False)
    about_me = models.CharField(max_length=500, default='Forever a mystery', blank=True)
    identifier = models.CharField(max_length=25, default='CIV-?')
    civ = models.BooleanField(default=False)
    police = models.BooleanField(default=False)
    ems = models.BooleanField(default=False)
    fire = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    user_type = models.CharField(max_length=10, default='user')

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()


#post_save.connect(create_profile, sender=User)
