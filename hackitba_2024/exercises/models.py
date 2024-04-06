from django.db import models
from user_auth.models import *

MEMORY = 'memory'
VISUALIZATION = 'visualization'

VALID_EXERCISES = [MEMORY, VISUALIZATION]

EXERCISE_TYPES = {
    MEMORY: 'Memoria',
    VISUALIZATION: 'Visualización'
}

class Exercise(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, choices=EXERCISE_TYPES)

    class Meta:
        abstract = True

STREAK = 'streak'
ACHIEV_AMOUNT = 'achiev_amount'
EXER_AMOUNT = 'exer_amount'
EXER_DIFF = 'exer_diff'
EXER_TYPE = 'exer_type'
EXER_DIFF_TYPE = 'exer_diff_type'

VALID_ACHIEVEMENTS = [STREAK, ACHIEV_AMOUNT, EXER_AMOUNT, EXER_DIFF, EXER_TYPE, EXER_DIFF_TYPE]

ACHIEVEMENT_TYPES = {
    STREAK: '',
    ACHIEV_AMOUNT: '',
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
    
    @property
    def is_completed(self):
        return self.progress == 100
    
class UserAchievement(models.Model):
    user = models.ForeignKey(UserProfile)
    achievement = models.ForeignKey(Achievement)
    progress = models.IntegerField(default=0)