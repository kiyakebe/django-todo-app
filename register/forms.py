from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

class RegiisterFrom(UserCreationForm):
    email: forms.EmailField()
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        