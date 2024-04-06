from django.db import models
from user_auth.models import *

# Exercises

MEMORY = 'memory'
VISUALIZATION = 'visualization'

VALID_EXERCISES = [MEMORY, VISUALIZATION]

EXERCISE_TYPES = {
    MEMORY: 'Memoria',
    VISUALIZATION: 'Visualización'
}

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, choices=EXERCISE_TYPES)

# Represents an instance of a specific exercise for a specific user.
class UserExercise(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    is_solved = models.BooleanField(default=False)


# Achievements

STREAK = 'streak'
ACHIV_AMOUNT = 'achiv_amount'
EXER_AMOUNT = 'exer_amount'
EXER_DIFF = 'exer_diff'
EXER_TYPE = 'exer_type'
EXER_DIFF_TYPE = 'exer_diff_type'

VALID_ACHIEVEMENTS = [STREAK, ACHIV_AMOUNT, EXER_AMOUNT, EXER_DIFF, EXER_TYPE, EXER_DIFF_TYPE]

ACHIEVEMENT_TYPES = {
    STREAK: 'Racha',
    ACHIV_AMOUNT: '',
    EXER_AMOUNT: '',
    EXER_DIFF: '',
    EXER_TYPE: '',
    EXER_DIFF_TYPE: '',
}

class Achievement(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField()
    limit = models.IntegerField(default=0)
    type = models.CharField(max_length=255, choices=ACHIEVEMENT_TYPES)

    def get_limit(self):
        return self.limit
    
    def set_limit(self, value):
        self.limit = value
    
    def get_type(self):
        return self.type
    
    def set_type(self, value):
        self.type = value
    
# Represents an instance of a specific achievement for a specific user.
class UserAchievement(models.Model):
    user = models.ForeignKey(UserProfile)
    achievement = models.ForeignKey(Achievement)
    progress = models.IntegerField(default=0)

    def get_progress(self):
        return self.progress

    def set_progress(self, value):
        self.progress = value

    @property
    def is_completed(self):
        return self.progress == 100