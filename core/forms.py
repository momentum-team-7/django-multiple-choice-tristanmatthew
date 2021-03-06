from django import forms
from .models import Profile, Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title','code','language', 'user']
