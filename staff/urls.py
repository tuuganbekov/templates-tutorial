from django.urls import path

from .views import create_staff

urlpatterns = [
    path('create/', create_staff)
]