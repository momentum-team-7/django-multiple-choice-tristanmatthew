from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Profile(request):
    name = models.CharField(max_length=280)
    snippet = models.ForeignKey('Snippet', on_delete=models.CASCADE, related_name='snippet')
    upload_date = models.TimeField()

    def __str__(self):
        return f"{self.name} | {self.snippet} | {self.upload_date}"

class Snippet(models.Model):
    code_desc = models.CharField(max_length=280)
    code_input = models.CharField(max_length=500)
    code_lang = models.CharField(max_length=280)

    def __str__(self):
        return f"{code_desc} | {self.code_input} | {self.code_lang}"

