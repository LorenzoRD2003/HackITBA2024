from django.urls import path, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
     path('info/', InfoView.as_view(), name='info'),
     path('achievements/', AchievementView.as_view(), name='achievements'),
     path('exercise/', ExerciseView.as_view(), name='exercises'),
     path('openai/', csrf_exempt(OpenAIView.as_view()), name='openai')
]