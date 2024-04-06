from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    FOCUS_CHOICES = (
        ('dyslexia', 'Dislexia'),
        ('alzheimer', "Alzheimer"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    streak = models.IntegerField(default=0)
    focus = models.CharField(max_length=200, choices=FOCUS_CHOICES)

    def __str__(self):
        return self.user.username