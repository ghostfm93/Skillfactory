from  django.contrib import admin
from django.urls import path,include
from django.contrib import flatpages

urlpatterns = [
    path('admin/', admin.site.urls),
]