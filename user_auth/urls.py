from django.urls import path, include
from django.contrib import admin

from .views import *

urlpatterns = [
     path('', CustomLoginView.as_view(), name='login'),
     path('register/', CustomRegisterView.as_view(), name='register'),
     path('logout/', LogoutView.as_view(), name='logout'),
]