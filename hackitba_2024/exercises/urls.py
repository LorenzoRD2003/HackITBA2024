from django.urls import path, include, re_path
from django.contrib import admin

from .views import *

urlpatterns = [
     path('info/', InfoView.as_view(), name='info'),
     path('achievements/', AchievementView.as_view(), name='achievements'),
     path('exercise/', ExerciseView.as_view(), name='exercises'),
     path('exercise/<str:ex_name>', ExerciseOneView.as_view(), name='ex1'),
     # path('exercise/ex4_<int:num>', ExerciseFourView.as_view(), name='ex4'),
     # re_path(r'exercise\/ex1_[0-9]+', ExerciseOneView.as_view(), name='ex1'),
     # re_path(r'exercise\/ex2_[0-9]+', ExerciseTwoView.as_view(), name='ex2'),
     # re_path(r'exercise\/ex3_[0-9]+', ExerciseThreeView.as_view(), name='ex3'),
     
]