from django.shortcuts import render
from math import floor

# Create your views here.
def percent_calc(act, total):
  return min(100, floor(act / total * 100))

def update_progress(user, achievement):
  