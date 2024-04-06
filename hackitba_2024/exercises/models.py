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

COMPLETED_10 = 'completed_10'
COMPLETED_20 = 'completed_20'

VALID_ACHIEVEMENTS = [COMPLETED_10, COMPLETED_20]

ACHIEVEMENT_TYPES = {
    COMPLETED_10: 'Completá 10 ejercicios',
    COMPLETED_20: 'Completá 20 ejercicios'
}

class Achievement(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    progress = models.IntegerField(default=0)
    limits = models.IntegerField(default=0)
    type = models.CharField(max_length=255, choices=ACHIEVEMENT_TYPES)
    
    @property
    def is_completed(self):
        return self.progress == 100