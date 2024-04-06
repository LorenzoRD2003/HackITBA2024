from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import *

class InfoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'info.html')


class ExerciseView(LoginRequiredMixin, View):
    pass

class AchievementView(LoginRequiredMixin, View):
    pass