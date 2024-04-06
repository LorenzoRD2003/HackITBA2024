from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import *

class InfoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'info.html')


class ExerciseView(LoginRequiredMixin, View):
    def get(self, request):
        # Dummy exercise data for testing
        exercise_list = [
            {
                'name': 'Exercise 1',
                'description': 'Description for Exercise 1',
                'image_url': 'img/crossword.png',
                'url': '/exercise/1'
            },
            {
                'name': 'Exercise 2',
                'description': 'Description for Exercise 2',
                'image_url': 'img/crossword.png',
                'url': '/exercise/2'
            },
            {
                'name': 'Exercise 3',
                'description': 'Description for Exercise 3',
                'image_url': 'img/crossword.png',
                'url': '/exercise/3'
            }
        ]

        context = {'exercise_list': exercise_list}
        return render(request, 'exercises.html', context)

class AchievementView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'achievements.html')