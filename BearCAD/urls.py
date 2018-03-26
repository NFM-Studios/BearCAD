from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.conf import settings
from django.conf.urls.static import settings
from civ import views as civ_views
from profiles import views as profile_views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', profile_views.CreateUserFormView.as_view(), name='register'),
    url(r'^login/', login, {'template_name': 'profiles/login_form.html'}, name='login'),
    url(r'^logout/', logout, {'template_name': 'index.html', 'next_page': '/'}, name='logout'),
    url(r'^reset-password/$', password_reset, {'template_name': 'profiles/reset_form.html', 'email_template_name': 'profiles/reset_email.html'}, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'profiles/reset_done.html'}, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'profiles/reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset-password/complete$', password_reset_complete, {'template_name': 'profiles/reset_complete.html'}, name='password_reset_complete'),
    url(r'^profile/', include('profiles.urls', namespace='profiles')),
    url(r"^activate/(?P<uidb64>[0-9A-Za-z_'\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$", profile_views.activate, name='activate'),


]
