from django.urls import path, include
from django.contrib import admin

from .views import HomeView

urlpatterns = [
     path('', HomeView.as_view(), name='home')
]