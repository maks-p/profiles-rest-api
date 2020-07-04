from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from djanjo.contrib.auth.models import PermissionsMixin


class UserProfile(AbstractBaseUser, PermissionsMixin):
  """Database model for users in the system"""
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_activate = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  