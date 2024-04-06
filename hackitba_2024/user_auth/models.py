from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  username = models.CharField(max_length=200, primary_key=True, default='test')
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  date_of_birth = models.DateField()
  streak = models.IntegerField(default=0)
  entered_today = models.BooleanField(default=0)
  FOCUS_CHOICES = (
    ('dyslexia', 'Dislexia'),
    ('alzheimer', "Alzheimer"),
  )
  focus = models.CharField(max_length=200, choices=FOCUS_CHOICES)
  
  def __str__(self):
    return self.user.username

  def get_username(self):
    return self.username
  
  def get_date_of_birth(self):
    return self.date_of_birth

  def get_streak(self):
    return self.streak

  def set_streak(self, value):
    self.streak = value
  
  def get_entered_today(self):
    return self.entered_today
  
  def set_entered_today(self, value):
    self.entered_today = value
  
  def get_focus(self):
    return self.focus[1]
  
  def set_focus(self, value):
    self.focus = value