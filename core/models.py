from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

  
class Profile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=150)
    date_added = models.TimeField()
    
    def __str__(self):
        return f"{self.name} | {self.date_added}"

class Snippet(models.Model):
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=1500)
    language = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="snippets")
    date_added = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

class Login(models.Model):
    username = models.CharField(max_length=8)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=10)

class Tag(models.Model):
    pass



    