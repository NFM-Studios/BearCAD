from django.contrib.auth.models import User
from django import forms
from .models import Civilian, Vehicle

class CreateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput)
    tos = forms.BooleanField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            #'profile_picture',
            'about_me',
        )

class CreateCivForm(forms.ModelForm):
    class Meta:

class EditCivForm(forms.ModelForm):
    

class CreateVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle


class EditVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = (
            'field_name'
        )
