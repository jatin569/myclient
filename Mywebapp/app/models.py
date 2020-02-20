
from django.contrib import auth

from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class signup(models.Model):
    Name = models.CharField(max_length=40)
    Username = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
    Password = models.CharField(max_length=40)

    def __str__(self):
        return self.Name +'==>' + self.Username +'==>' + self.Email +'==>' + self.Password

class login(models.Model):
    Name = models.CharField(max_length=40)
    Password = models.CharField(max_length=40)
    Submit = models.CharField(max_length=40)