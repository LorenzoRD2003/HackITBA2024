from django.db import models
from user_auth.models import *

class Exercise(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        abstract = True

class Achievement(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    progress = models.IntegerField(default=0)
    limits = models.IntegerField(default=0)

    class Meta:
        abstract = True
    
    @property
    def is_completed(self):
        return self.progress == 100