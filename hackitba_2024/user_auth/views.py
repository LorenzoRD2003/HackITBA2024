from .models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

class CustomLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('info'))
        
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
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
        focus = request.POST.get('focus')
        
        if not (username and password and date_of_birth and focus):
            return JsonResponse({'error': 'Missing required fields'}, status=400)   

        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            UserProfile.objects.create(
                username = user.username,
                user = user,
                date_of_birth = date_of_birth,
                streak = 0
            )
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
        login(request, user)
        return redirect('info')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')