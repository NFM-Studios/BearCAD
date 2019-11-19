from django.db import models
from profiles.models import PersonProfile, UserProfile


class UserVehicleMakeChoice(models.Model):
    name = models.CharField(default="vehicle make", max_length=255)


class UserVehicleModelChoice(models.Model):
    name = models.CharField(default="vehicle model", max_length=255)


class UserVehicle(models.Model):
    make = models.ForeignKey(UserVehicleMakeChoice, related_name='uservehicle_make', on_delete=models.SET_NULL,
                             null=True)
    model = models.ForeignKey(UserVehicleModelChoice, related_name='uservehicle_model', on_delete=models.SET_NULL,
                              null=True)


class MapCountyOption(models.Model):
    name = models.CharField(default="CountyOption", max_length=255)


class MapStreetOption(models.Model):
    name = models.CharField(default="StreetOption", max_length=255)
    county = models.ForeignKey(MapCountyOption, related_name='street_county', on_delete=models.SET_NULL, null=True)
    postal = models.CharField(null=True, blank=True, max_length=10)


class Department(models.Model):
    name = models.CharField(max_length=255, default="Default Department Name")
    short = models.CharField(null=True, blank=True, max_length=255)
    max_size = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(default="No department description")
    # TODO - LOGO/Image Field for Department


class UnitStatusOption(models.Model):
    code = models.CharField(default="10-8", max_length=20)
    description = models.CharField(default="Available", max_length=255)


class DepartmentUnit(models.Model):
    callsign = models.CharField(default='1A-25', max_length=50)
    status = models.PositiveSmallIntegerField(default=0)


class CallReport(models.Model):
    info = models.TextField(default='Call Report')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class IncidentType(models.Model):
    # number = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=255, default="Robbery")


class Call(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # TODO - verify on_delete set null
    creator = models.ForeignKey(PersonProfile, related_name='call_creator', on_delete=models.SET_NULL, null=True)
    departments = models.ManyToManyField(Department)
    reports = models.ManyToManyField(CallReport)
    street1 = models.ForeignKey(MapStreetOption, related_name='MAP_STREET_1', on_delete=models.SET_NULL, null=True)
    street2 = models.ForeignKey(MapStreetOption, related_name='MAP_STREET_2', on_delete=models.SET_NULL, null=True)
    street_other = models.CharField(blank=True, null=True, max_length=255)
    units = models.ManyToManyField(DepartmentUnit)
    incident_type = models.ForeignKey(IncidentType, related_name='CALL_INCIDENT', on_delete=models.SET_NULL, null=True)


class CitationType(models.Model):
    name = models.CharField(default="Citation Type", max_length=100)
    description = models.CharField(default="Citation Description", max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Citation(models.Model):
    person = models.ForeignKey(PersonProfile, related_name='citation_person', on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(PersonProfile, related_name='citation_creator', on_delete=models.SET_NULL, null=True)
    department_issuing = models.ForeignKey(Department, related_name='citation_issuing_department',
                                           on_delete=models.SET_NULL,
                                           null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(default="no warning description description")
    type = models.ManyToManyField(CitationType)


class WarningType(models.Model):
    name = models.CharField(default="Warning Type", max_length=100)
    description = models.CharField(default="Warning Description", max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Warning(models.Model):
    person = models.ForeignKey(PersonProfile, related_name='warning_person', on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(PersonProfile, related_name='warning_creator', on_delete=models.SET_NULL, null=True)
    department_issuing = models.ForeignKey(Department, related_name='wawrning_issuing_department',
                                           on_delete=models.SET_NULL,
                                           null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(default="no warning description description")
    type = models.ManyToManyField(WarningType)


class WarrantType(models.Model):
    name = models.CharField(default="Warrant Type", max_length=100)
    description = models.CharField(default="Warrant Description", max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Warrant(models.Model):
    person = models.ForeignKey(PersonProfile, related_name='wanted_person', on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(PersonProfile, related_name='warrant_creator', on_delete=models.SET_NULL, null=True)
    department_issuing = models.ForeignKey(Department, related_name='warrant_issuing_department',
                                           on_delete=models.SET_NULL,
                                           null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(default="no warrant description")
    type = models.ManyToManyField(WarrantType)
    call = models.ManyToManyField(Call)
