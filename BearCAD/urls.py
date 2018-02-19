from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.conf import settings
from django.conf.urls.static import settings
from civ import views as civ_views
from profiles import views as profile_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),


]
