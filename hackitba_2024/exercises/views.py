from django.shortcuts import render
from math import floor

from models import *

# Create your views here.
def percent_calc(act, total):
  return min(100, floor(act / total * 100))

def update_progress(username, achiv_name):
  user = User.objects.filter(user_id = username)
  achiv = Achievement.objects.filter(achievement_id = achiv_name)
  user_achiv = UserAchievement.objects.filter(user_id = username, achievement_id = achiv_name)
  
  if (user_achiv.progress == 100):
    return
  
  
  
  user_achiv.save()