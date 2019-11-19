from django.db import models
from django.contrib.auth.models import User
#from cad.models import Department, UserVehicle


class PersonProfile(models.Model):
    first = models.CharField(default="First", max_length=20)
    last = models.CharField(default="Last", max_length=20)
    #departments = models.ManyToManyField(Department)
    # warrants = mtm
    #vehicles = models.ManyToManyField(UserVehicle)
    # addresses
    # permits


class UserProfile(models.Model):
    def __str__(self):
        return str(self.user)

    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    # email_verified = models.BooleanField(default=False)
    about_me = models.CharField(max_length=500, default='Forever a mystery', blank=True)
    approved = models.BooleanField(default=False)
    user_type = models.CharField(max_length=10, default='user')
    persons = models.ManyToManyField(PersonProfile)
    bio = models.TextField(default="User hasn't set a bio yet")


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()

# post_save.connect(create_profile, sender=User)
