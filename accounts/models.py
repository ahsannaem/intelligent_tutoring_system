from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Use OneToOneField for a user profile
    rank = models.PositiveSmallIntegerField(default=0)  # 0 --> beginner, 1 --> intermediate, 2 --> advanced
    quiz_count = models.PositiveSmallIntegerField(default=0)  # Optional: Set default value
    badge = models.PositiveSmallIntegerField(default=0)  # 0 --> silver, 1 --> bronze, 2 --> gold

    def __str__(self):
        return f"{self.user.username}'s Profile"

    # Optional: you might not need a custom __init__
    # Django handles model instantiation with fields automatically
