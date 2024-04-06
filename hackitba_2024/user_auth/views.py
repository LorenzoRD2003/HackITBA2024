from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from models import *
from .forms import UserRegistrationForm, LoginForm

# Create your views here.
class UserRegistrationView(View):
  form_class = UserRegistrationForm
  template_name = "registration.html"

  def get(self, request):
    form = LoginForm()
    return render(request, self.template_name, {"form": form})

  def post(self, request):
    form = UserRegistrationForm(data = request.POST)
    if form.is_valid():
      # <process form cleaned data>
      return HttpResponseRedirect("/success/")
    return render(request, self.template_name, {"form": form})

class LoginView(View):
  template_name = 'login.html'

  def get(self, request):
    form = LoginForm()
    return render(request, self.template_name, {'form': form})

  def post(self, request):
    form = LoginForm(data = request.POST)
    if form.is_valid():
      # Handle successful login
      return HttpResponseRedirect('/success/')  # Redirect to success page
    return render(request, self.template_name, {'form': form})
