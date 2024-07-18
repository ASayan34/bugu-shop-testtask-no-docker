from django.contrib.auth.models import AbstractUser
from django.db import models
from account.models import CustomUser


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_public = models.BooleanField(default=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
