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
  
  if (user_achiv.is_completed()):
    return
  
  if (achiv.get_type() == STREAK):
    act = user.get_streak()
  elif (achiv.get_type() == ACHIV_AMOUNT):
    act = UserAchievement.objects.filter(user_id = username).count()
  elif (achiv.get_type() == EXER_AMOUNT):
    act = UserExercise.objects.filter(user_id = username).count()
  elif (achiv.get_type() == EXER_DIFF):
    act = Exercise.objects.filter(userexercise__username=username,
                                  userexercise__difficulty=achiv.get_difficulty()).count()
  elif (achiv.get_type() == EXER_TYPE):
    act = Exercise.objects.filter(userexercise__username=username,
                                  userexercise__type=achiv.get_type()).count()
  elif (achiv.get_type() == EXER_DIFF_TYPE):
    act = Exercise.objects.filter(userexercise__username=username,
                                  userexercise__difficulty=achiv.get_difficulty(),
                                  userexercise__type=achiv.get_type()).count()
  
  user_achiv.set_progress(percent_calc(act + 1, achiv.get_limit()))
  user_achiv.save()
  if (user_achiv.is_completed()):
    update_progress(user, ACHIV_AMOUNT)

STREAK_ACHIEVEMENTS_DAYS = (5, 10, 25, 50, 100, 365)

# Function to be executed every day
def remove_streak(username):
  user = User.objects.filter(user_id = username)
  user.set_streak(0)
  user.save()
  for s in STREAK_ACHIEVEMENTS_DAYS:
    update_progress(username, f"STREAK_{s}")

def change_day():
  for user in User.object.all():
    if user.get_entered_today() == False:
      remove_streak(user)
    else:
      user.set_entered_today(False)
      user.save()
