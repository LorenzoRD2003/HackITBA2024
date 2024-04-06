import sys
sys.path.append("..")

from time import sleep
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from user_auth.models import *
from exercises.models import *
from exercises.utils import *

class InfoView(LoginRequiredMixin, View):
  def get(self, request):
    return render(request, 'info.html')


class ExerciseView(LoginRequiredMixin, View):
  def get(self, request):
    username = request.user.username
    user = UserProfile.objects.get(pk = username)

    exercises = list(Exercise.objects.all())
    
    db_list = list(map(lambda exer: exer.generate_object(user), exercises))
    return render(request, 'exercises.html', {
      'exercise_list': db_list
    })

class AchievementView(LoginRequiredMixin, View):
  def get(self, request):    
    user = UserProfile.objects.get(pk = request.user.username)
    
    # Later, we can make filters on the next line
    achievements = list(Achievement.objects.all())
    
    db_list = list(map(lambda achiv: achiv.generate_object(user), achievements))
    return render(request, 'achievements.html', {
      'achievement_list': db_list
    })

class ExerciseOneView(LoginRequiredMixin, View):
  def get(self, request):
    user = UserProfile.objects.get(pk = request.user.username)
    exercise_name = request.GET.get('exercise')
    exercise = Exercise.objects.get(pk = exercise_name)
    
    exercise_data = exercise.generate_object(user)
    difficulty = exercise.get_difficulty()
    if (difficulty == BEGINNER):
      # Read and parse info from ex1_beginner.txt
      questions = read_and_parse("ex1_beginner", 5)
    elif (difficulty == INTERMEDIATE):
      # Read and parse info from ex1_intermediate.txt
      questions = read_and_parse("ex1_intermediate", 10)
    elif (difficulty == ADVANCED):
      # Read and parse info from ex1_advanced.txt
      questions = read_and_parse("ex1_advanced", 20)
    
    return render(request, "ex1.html", {
      'exercise_data': exercise_data,
      "questions": questions
    })

class ExerciseTwoView(LoginRequiredMixin, View):
  def get(self, request):
    user = UserProfile.objects.get(pk = request.user.username)
    exercise_name = request.GET.get('exercise')
    exercise = Exercise.objects.get(pk = exercise_name)
    
    exercise_data = exercise.generate_object(user)
    
    return render(request, "ex1.html", {
      'exercise_data': exercise_data
    })

class ExerciseThreeView(LoginRequiredMixin, View):
  def get(self, request):
    user = UserProfile.objects.get(pk = request.user.username)
    exercise_name = request.GET.get('exercise')
    exercise = Exercise.objects.get(pk = exercise_name)
    
    exercise_data = exercise.generate_object(user)
    
    return render(request, "ex1.html", {
      'exercise_data': exercise_data
    })

class ExerciseFourView(LoginRequiredMixin, View):
  def get(self, request):
    user = UserProfile.objects.get(pk = request.user.username)
    exercise_name = request.GET.get('exercise')
    exercise = Exercise.objects.get(pk = exercise_name)
    
    exercise_data = exercise.generate_object(user)
    
    return render(request, "ex1.html", {
      'exercise_data': exercise_data
    })
