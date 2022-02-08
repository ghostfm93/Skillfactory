from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import auth_login, logout_then_login, auth_logout
from django.contrib.auth import views
urlpatterns = [
    # path('register', register, name='register'),
    # path('login', views.user_login, name='login'),
    path('login/',auth_login , name='login'),
    url(r'^logout/$', auth_logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    ]