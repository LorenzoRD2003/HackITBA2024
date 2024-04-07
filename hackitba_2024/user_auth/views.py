from .models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

import datetime

import math
import random

from exercises.models import UserAchievement, Achievement, Exercise, UserExercise
from exercises.utils import create_achievement

def update_streak(username):
    user_profile = UserProfile.objects.get(pk=username)
    time_difference = abs(user_profile.last_login - datetime.datetime.now())

    # Define a timedelta representing one day
    one_day = datetime.timedelta(days=1)

    # Check if the time difference is less than one day
    if time_difference < one_day:
        user_profile.streak += 1
    
    else:
        user_profile.streak = 0

    user_profile.save()

class CustomLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            update_streak(request.user.username)
            return redirect(reverse('exercises'))
        
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            update_streak(username)

            login(request, user)
            return redirect('info') 
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})

class CustomRegisterView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        
        if not (username and password and date_of_birth):
            return JsonResponse({'error': 'Missing required fields'}, status=400)   

        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user_profile = UserProfile.objects.create(
                username = user.username,
                user = user,
                date_of_birth = date_of_birth,
                streak = 0
            )

            # --- Crear todo ---
            achivs = Achievement.objects.all()
            exers = Exercise.objects.all()

            for achiv in achivs:
                print('Create user achievement')
                UserAchievement.objects.create(user=user_profile, achievement=achiv, progress=math.floor(random.random() * achiv.limit))

            for exer in exers:
                print('Creat user exercise')
                UserExercise.objects.create(user=user_profile, exercise=exer)

            # --------


        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        login(request, user)
        return redirect('exercises')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')