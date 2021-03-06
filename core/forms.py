from django import forms
from .models import Profile, Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['snip_desc','snip_input','snip_lang', 'user', 'snip_added']
