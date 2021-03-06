from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

  
class Profile(models.Model):
    name = models.CharField(max_length=150)
    snippet = models.ForeignKey("Snippet", on_delete=models.CASCADE, related_name="snippet")
    date_added = models.DateTimeField()
    
    def __str__(self):
        return f"{self.name} | {self.snippet} | {self.date_added}"

class Snippet(models.Model):
    snip_desc = models.CharField(max_length=300, null=True)
    snip_lang = models.CharField(max_length=100, null=True)
    snip_input = models.CharField(max_length=1500, null=True)
    snip_added = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippets')

    def __str__(self):
        return f"{self.snip_desc} | {self.snip_input} | {self.snip_lang}"