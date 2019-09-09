from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Ovdje nasljedjujem original forms koji je koristi na admin pageu
# i dodajem svoja polja koja zelim vidjeti tamo


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
