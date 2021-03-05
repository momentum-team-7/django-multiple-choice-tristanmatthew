from django import forms
from .models import Profile, Snippet

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']