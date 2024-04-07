from django.urls import path, include, re_path
from django.contrib import admin

from .views import *

urlpatterns = [
     path('info/', InfoView.as_view(), name='info'),
     path('achievements/', AchievementView.as_view(), name='achievements'),
     path('exercise/', ExerciseView.as_view(), name='exercises'),
     path('exercise/ex1_<str:ex_num>', ExerciseOneView.as_view(), name='ex1'),
     path('exercise/ex2_<str:ex_num>', ExerciseTwoView.as_view(), name='ex2'),
     path('exercise/ex3_<str:ex_num>', ExerciseThreeView.as_view(), name='ex3'),
     path('exercise/ex4_<str:ex_num>', ExerciseFourView.as_view(), name='ex4'),
]