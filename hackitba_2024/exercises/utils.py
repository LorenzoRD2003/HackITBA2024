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
    act = user.streak
  elif (achiv.get_type() == ACHIV_AMOUNT):
    act = UserAchievement.objects.filter(user_id = username).count()
  elif (achiv.get_type() == EXER_AMOUNT):
    act = get_exer_amount(user)
  elif (achiv.get_type() == EXER_DIFF):
    act = get_exer_amount(user, exer_diff)
  elif (achiv.get_type() == EXER_TYPE):
    act = get_exer_amount(user, exer_type)
  elif (achiv.get_type() == EXER_DIFF_TYPE):
    act = get_exer_amount(user, exer_diff, exer_type)
  
  user_achiv.set_progress(percent_calc(act + 1, achiv.limit))
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
