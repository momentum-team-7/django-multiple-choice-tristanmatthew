from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

  
class Profile(models.Model):
    name = models.CharField(max_length=150)
    snippet = models.ForeignKey("Snippet", on_delete=models.CASCADE, related_name="snippet")
    date_added = models.TimeField()
    
    def __str__(self):
        return f"{self.name} | {self.snippet} | {self.date_added}"

class Snippet(models.Model):
    code_desc = models.CharField(max_length=300)
    code_input = models.CharField(max_length=1500)
    code_lang = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code_desc} | {self.code_input} | {self.code_lang}"