from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=128, blank=True)

    def  __str__(self):
        return self.username
