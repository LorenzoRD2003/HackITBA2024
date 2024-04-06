from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import *
from .utils import *

class InfoView(LoginRequiredMixin, View):
  def get(self, request):
    return render(request, 'info.html')


class ExerciseView(LoginRequiredMixin, View):
  def get(self, request):
    user = UserProfile.objects.get(pk = request.user.username)
  
    # Later, we can make filters on the next line
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
      questions = read_and_parse_ex1("ex1_beginner", 5)
    elif (difficulty == INTERMEDIATE):
      # Read and parse info from ex1_intermediate.txt
      questions = read_and_parse_ex1("ex1_intermediate", 10)
    elif (difficulty == ADVANCED):
      # Read and parse info from ex1_advanced.txt
      questions = read_and_parse_ex1("ex1_advanced", 20)
    
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
    difficulty = exercise.get_difficulty()
    if (difficulty == BEGINNER):
      questions = read_and_parse_ex2("ex2_beginner", 6)
    elif (difficulty == INTERMEDIATE):
      questions = read_and_parse_ex2("ex2_intermediate", 6)
    elif (difficulty == ADVANCED):
      questions = read_and_parse_ex2("ex2_advanced", 6)
    
    return render(request, "ex2.html", {
      'exercise_data': exercise_data,
      "questions": questions
    })

class ExerciseThreeView(LoginRequiredMixin, View):
  def get(self, request):
    user = UserProfile.objects.get(pk = request.user.username)
    exercise_name = request.GET.get('exercise')
    exercise = Exercise.objects.get(pk = exercise_name)
    
    exercise_data = exercise.generate_object(user)
    difficulty = exercise.get_difficulty()
    if (difficulty == BEGINNER):
      questions = read_and_parse_ex3("ex3", 1)
    elif (difficulty == INTERMEDIATE):
      questions = read_and_parse_ex3("ex3", 4)
    elif (difficulty == ADVANCED):
      questions = read_and_parse_ex3("ex3", 10)
    
    return render(request, "ex2.html", {
      'exercise_data': exercise_data,
      "questions": questions
    })

class ExerciseFourView(LoginRequiredMixin, View):
  def get(self, request):
    user = UserProfile.objects.get(pk = request.user.username)
    exercise_name = request.GET.get('exercise')
    exercise = Exercise.objects.get(pk = exercise_name)
    
    exercise_data = exercise.generate_object(user)
    difficulty = exercise.get_difficulty()
    if (difficulty == BEGINNER):
      questions = read_and_parse_ex4("ex4_beginner")
    elif (difficulty == INTERMEDIATE):
      questions = read_and_parse_ex4("ex4_intermediate")
    elif (difficulty == ADVANCED):
      questions = read_and_parse_ex4("ex4_advanced")
    
    return render(request, "ex2.html", {
      'exercise_data': exercise_data,
      "questions": questions
    })
