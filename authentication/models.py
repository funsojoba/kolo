import uuid
from django.db import models

# from helpers.db_helpers import BaseAbstractModel

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
    def create_user(self, email, password=None, **extrafields):
        extrafields.setdefault("is_superuser", False)
        return self._create_user(email=email, password=password, **extrafields)

    def create_superuser(self, email, password=None, **extrafields):
        extrafields.setdefault("is_superuser", True)
        extrafields.setdefault("is_active", True)
        extrafields.setdefault("is_staff", True)
        return self._create_user(email=email, password=password, **extrafields)
    

class User( AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
        
    