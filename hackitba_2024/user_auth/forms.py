from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
  date_of_birth = forms.DateField(label='Date of Birth', required=False, widget=forms.DateInput(attrs={'type': 'date'}))

  class Meta:
    model = User
    fields = ['username', 'password1', 'password2', 'date_of_birth']

  def save(self, commit=True):
    user = super().save(commit=False)
    if commit:
      user.save()
      UserProfile.objects.create(user=user, date_of_birth=self.cleaned_data['date_of_birth'])
    return user