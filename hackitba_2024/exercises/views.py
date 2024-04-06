from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

class InfoView(LoginRequiredMixin, View):
    pass

class ExerciseView(LoginRequiredMixin, View):
    pass

class AchievementView(LoginRequiredMixin, View):
    pass