from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

class HomeView(LoginRequiredMixin, View):
  