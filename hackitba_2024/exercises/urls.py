from django.urls import path, include, re_path
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
     path('info/', InfoView.as_view(), name='info'),
     path('achievements/', AchievementView.as_view(), name='achievements'),
     path('exercise/', ExerciseView.as_view(), name='exercises'),
     path('exercise/ex1_<int:ex_num>', ExerciseOneView.as_view(), name='ex1'),
     path('exercise/ex2_<int:ex_num>', ExerciseTwoView.as_view(), name='ex2'),
     path('exercise/ex3_<int:ex_num>', ExerciseThreeView.as_view(), name='ex3'),
     path('exercise/ex4_<int:ex_num>', ExerciseFourView.as_view(), name='ex4'),
]