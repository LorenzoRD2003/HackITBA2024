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
    # Dummy exercise data for testing
    exercise_list = [
      {
        'name': 'Exercise 1',
        'description': 'Description for Exercise 1',
        'difficulty': 'Difficulty for exercise',
        'image_url': 'img/rubik.png',
        'type': 'Type for exercise',
        'is_solved': 0,
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
      },
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
      },
      {
        'name': 'Exercise 1',
        'description': 'Description for Exercise 1',
        'image_url': 'img/crossword.png',
        'url': '/exercise/1'
      },
      {
        'name': 'Exercise 2',
        'description': 'Description for Exercise 2',
        'image_url': 'img/rubik.png',
        'url': '/exercise/2'
      },
      {
        'name': 'Exercise 3',
        'description': 'Description for Exercise 3',
        'image_url': 'img/crossword.png',
        'url': '/exercise/3'
      }
    ]
    
    # Later, we can make filters on the next line
    exercises = list(Exercise.object.all())
    
    db_list = list(map(lambda exer: exer.generate_object(user), exercises))
    return render(request, 'exercises.html', {
      'exercise_list': db_list
    })

class AchievementView(LoginRequiredMixin, View):
  def get(self, request):
    achievement_list = [
      {
        'name': 'Achievement 1',
        'description': 'Description for Achievement 1',
        'difficulty': 'BEGINNER',
        'progress': 0,
        'type': '...',
        'url': '/exercise/1'
      },
      {
        'name': 'Exercise 2',
        'description': 'Description for Exercise 2',
        'difficulty': 'INTERMEDIATE',
        'progress': 0,
        'type': '...',
        'url': '/exercise/2'
      },
      {
        'name': 'Exercise 3',
        'description': 'Description for Exercise 3',
        'difficulty': 'ADVANCED',
        'progress': 0,
        'type': '...',
        'url': '/exercise/3'
      }
    ]
    
    user = UserProfile.objects.get(pk = request.user.username)
    
    # Later, we can make filters on the next line
    achievements = list(Achievement.object.all())
    
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
