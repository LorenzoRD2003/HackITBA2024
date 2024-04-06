from math import floor

STREAK_ACHIEVEMENTS_DAYS = (5, 10, 25, 50, 100, 365)

def percent_calc(act, total):
  return min(100, floor(act / total * 100))

def update_progress(user, achievement):
  if (completed_achievement(user, achievement)):
    return
  
  if (achievement.startswith("streak")):
    act = get_streak(user)
  elif (achievement.startswith("achiev_amount")):
    act = get_achiev_amount(user)
  elif (achievement.startswith("exer_amount")):
    act = get_exer_amount(user)
  elif (achievement.startswith("exer_diff")):
    act = get_exer_amount(user, exer_diff)
  elif (achievement.startswith("exer_type")):
    act = get_exer_amount(user, exer_type)
  elif (achievement.startswith("exer_diff_type")):
    act = get_exer_amount(user, exer_diff, exer_type)
  else:
    print("ERROR xd")
  
  act = act + 1
  total = get_number(achievement)
  progress = percent_calc(act, total)
  if (progress == 100)
    get_achiev(user, achievement)
    update_progress(user, "achiev_amount_...")

def solve_exercise(user, exercise):
  update_progress(user, "exer_amount")
  update_progress(user, f"exer_diff_{exercise.diff}")
  update_progress(user, f"exer_type_{exercise.type}")
  update_progress(user, f"exer_diff_{exercise.diff}_type_{exercise.type}")

def login(user):
  if (user.entered_today == False):
    user.entered_today = True
    for s in STREAK_ACHIEVEMENTS_DAYS:
      update_progress(user, f"streak_{s}")

# Function to be executed on day change
def change_day():
  for user in get_all_users():
    update_progress(user, f"streak_")


