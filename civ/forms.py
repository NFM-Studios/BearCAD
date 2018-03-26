from django.contrib.auth.models import User
from django import forms
from .models import Civilian, Vehicle

class CreateCivForm(forms.ModelForm):
    class Meta:
        model = Civilian
        fields = (
            'field_name',
        )

class EditCivForm(forms.ModelForm):
    class Meta:
        model = Civilian
        fields = (
            'field_name',
        )

class CreateVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = (
            'field_name'
        )


class EditVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = (
            'field_name',
        )
