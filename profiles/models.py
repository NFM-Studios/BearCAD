from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    def __str__(self):
        return str(self.user)
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    use_2fa = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    about_me = models.CharField(max_length=500, default='Forever a mystery', blank=True)
    identifier = models.CharField(max_length=25, default='CIV-?')
    approved = models.BooleanField(default=False)
    user_type = models.CharField(max_length=10, default='user')
    ip = models.CharField(max_length=16, default='0.0.0.0')

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()

class BannedUser(models.Model):
    user = models.ForeignKey(User, related_name='banned', on_delete=models.CASCADE)
    ip = models.CharField(max_length=12, default='error')



post_save.connect(create_profile, sender=User)
