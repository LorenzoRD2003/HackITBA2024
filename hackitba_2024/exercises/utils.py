from math import floor
from .models import *
import random

import os


# Create your views here.
def percent_calc(act, total):
  return min(100, floor(act / total * 100))

def update_progress(username, achiv_name):
  user = User.objects.get(pk = username)
  achiv = Achievement.objects.get(pk = achiv_name)
  user_achiv = UserAchievement.objects.filter(user_id = username, achievement_id = achiv_name).first()
  
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

def increase_streak(username):
  user = UserProfile.objects.get(pk = username)
  user.set_streak(user.set_streak() + 1)
  user.save()
  for s in STREAK_ACHIEVEMENTS_DAYS:
    update_progress(username, f"STREAK_{s}")

# Function to be executed every day
def remove_streak(username):
  user = UserProfile.objects.get(pk = username)
  user.set_streak(0)
  user.save()
  for s in STREAK_ACHIEVEMENTS_DAYS:
    update_progress(username, f"STREAK_{s}")


def create_achievement(achiv_description, achiv_limit, achiv_type, achiv_exer_difficulty=1):
  if (achiv_type not in VALID_ACHIEVEMENTS):
    return print("Invalid achievement type.")
  achiv_name = f"{achiv_type}_{achiv_limit}"
  Achievement.objects.create(
    name = achiv_name,
    description = achiv_description,
    limit = achiv_limit,
    type = achiv_type,
    exer_difficulty = achiv_exer_difficulty,
  )

def delete_achievement(achiv_name):
  achiv = Achievement.objects.get(pk = achiv_name)
  achiv.delete()

def create_exercise(exer_title, exer_description, exer_difficulty, exer_type, exer_image, num=1):
  if (exer_difficulty not in VALID_DIFFICULTIES):
    return print("Invalid exercise difficulty.")

  exer_name = f"{exer_type}_{num}"
  Exercise.objects.create(
    name = exer_name,
    title = exer_title,
    description = exer_description,
    difficulty = exer_difficulty,
    type = exer_type,
    image = exer_image
  )

def delete_exercise(exer_name):
  exercise = Exercise.objects.get(pk = exer_name)
  exercise.delete()


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
def read_and_parse_ex1(filename, word_amount):
  try:
    with open(f'{dname}/texto/{filename}.txt', 'r') as file:
      text_content = file.read().upper().split('\n')
  except FileNotFoundError:
    return []
  filtered = random.sample(text_content, k = word_amount)
  parsed = list(map(lambda pair: tuple(pair.split(',')), filtered))
  corrected = list(map(lambda p: [
    {
      'text': p[0],
      'correct': True
    },
    {
      'text': p[1],
      'correct': False
    }
  ], parsed))
  reordered = list(map(lambda p: random.sample(p, k=len(p)), corrected))
  return reordered

def read_and_parse_ex2(filename, amount):
  try:
    with open(f'{dname}/texto/{filename}.txt', 'r') as file:
      text_content = file.read().upper().split('\n')
  except FileNotFoundError:
    return []
  # Three words, one image
  filtered = random.sample(text_content, k = amount)
  splitted = list(map(lambda pair: tuple(pair.split(',')), filtered))
  parsed = list(map(lambda p: {
    'options': [
      {
        'text': p[0],
        'correct': True
      },
      {
        'text': p[1],
        'correct': False
      },
      {
        'text': p[2],
        'correct': False
      }
    ],
    "image": p[3]
  }, splitted))
  for p in parsed:
    p["options"] = random.sample(p["options"], k = len(p["options"]))
  return parsed

def read_and_parse_ex3(filename, amount):
  try:
    with open(f'{dname}/texto/{filename}.txt', 'r') as file:
      text_content = file.read().upper().split('\n')
  except FileNotFoundError:
    return []
  filtered = random.sample(text_content, k = amount)
  without_spaces = list(map(lambda phrase: phrase.replace(' ', ''), filtered))
  return {
    "original": filtered,
    "without_spaces": without_spaces
  }

def read_and_parse_ex4(filename):
  try:
    with open(f'{dname}/texto/{filename}.txt', 'r') as file:
      text_content = file.read().upper().split('\n')
  except FileNotFoundError:
    return []
  return random.sample(text_content, k = 1)[0]
