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
    Title = models.CharField(max_length=300)
    Input = models.CharField(max_length=1500)
    Language = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Title

class Login(models.Model):
    username = models.CharField(max_length=8)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=10)

    class Tag(models.Model):
        pass



    