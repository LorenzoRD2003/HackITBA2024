from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import UserProfile

class CustomLoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})

class CustomRegisterView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        date_of_birth = request.POST.get('date_of_birth')
        focus = request.POST.get('focus')
        
        if not (username and password and date_of_birth and focus):
            return JsonResponse({'error': 'Missing required fields'}, status=400)   

        try:
            user = User.objects.create_user(username=username, password=password)
            UserProfile.objects.create(
                user=user,
                date_of_birth=date_of_birth,
                streak=0
            )
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        login(request, user)
        return redirect('home')
