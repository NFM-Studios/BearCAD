from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views as views

app_name = 'staff'

urlpatterns = [
    path('', login_required(views.staffindex), name='index'),

]
