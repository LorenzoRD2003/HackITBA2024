from django.db import models
from user_auth.models import *

# Exercises
NONE = -1
BEGINNER = 0
INTERMEDIATE = 1
ADVANCED = 2

MEMORY = 'memory'
VISUALIZATION = 'visualization'

VALID_DIFFICULTIES = (NONE, BEGINNER, INTERMEDIATE, ADVANCED)
VALID_EXERCISES = (MEMORY, VISUALIZATION)

EXERCISE_DIFFICULTIES = {
    BEGINNER: 'Principiante',
    INTERMEDIATE: "Intermedio",
    ADVANCED: "Avanzado"
}

EXERCISE_TYPES = {
    MEMORY: 'Memoria',
    VISUALIZATION: 'Visualización'
}

class Exercise(models.Model):
    name = models.CharField(max_length=255, primary_key = True)
    description = models.TextField()
    type = models.CharField(max_length=255, choices=EXERCISE_TYPES)
    difficulty = models.IntegerField(default=0)

    def get_name(self):
        return self.name
    
    def set_name(self, value):
        self.name = value
    
    def get_description(self):
        return self.description
    
    def set_description(self, value):
        self.description = value

    def get_type(self):
        return self.type
    
    def set_type(self, value):
        if (value not in VALID_EXERCISES):
            return print("Invalid exercise type.")
        self.type = value
    
    def get_difficulty(self):
        return self.difficulty
    
    def set_difficulty(self, value):
        if (value not in VALID_DIFFICULTIES):
            return print("Invalid exercise difficulty.")
        self.difficulty = value
    
    # Util for returning exercise as an object and give it to the frontend
    def generate_object(self, user):
        user_exercise = UserExercise.objects.filter(
            user_id = user.username,
            exercise_id = self.name).first()
        return {
            'name': self.name,
            'description': self.description,
            'difficulty': self.difficulty,
            'image_url': 'img/rubik.png',
            'type': self.type,
            'is_solved': user_exercise.is_solved,
            'url': f'/exercise/{self.name}'
        }

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

VALID_ACHIEVEMENTS = (STREAK, ACHIV_AMOUNT, EXER_AMOUNT, EXER_DIFF, EXER_TYPE, EXER_DIFF_TYPE)

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
    type = models.CharField(max_length=255, choices=ACHIEVEMENT_TYPES, blank=True)
    exer_difficulty = models.IntegerField(default=None, choices=EXERCISE_DIFFICULTIES, blank=True)
    exer_type = models.CharField

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value
    
    def get_description(self):
        return self.description
    
    def set_description(self, value):
        self.description = value

    def get_limit(self):
        return self.limit
    
    def set_limit(self, value):
        self.limit = value
    
    def get_type(self):
        return self.type
    
    def set_type(self, value):
        if (value not in VALID_ACHIEVEMENTS):
            return print("Invalid achievement type.")
        self.type = value
    
    # Util for returning achievement as an object and give it to the frontend
    def generate_object(self, user):
        user_achiv = UserAchievement.objects.filter(
        user_id = user.username,
        achievement_id = self.name).first()
        return {
            'name': self.name,
            'description': self.description,
            'exer_difficulty': self.exer_difficulty,
            'exer_type': self.exer_type,
            'progress': user_achiv.progress,
            'type': self.type,
            'url': f'/exercise/{self.name}'
        }
    
# Represents an instance of a specific achievement for a specific user.
class UserAchievement(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)
