from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class LockinUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.__db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_supseruser", True)
        return self.create_superuser(email, password, **extra_fields)

class LockinUser(AbstractUser):
    email = models.EmailField(unique=True)
    lockin_activities = models.CharField(max_length=128, default="Empty")
    user_photo = models.ImageField(upload_to="uploads/", null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = LockinUserManager

    @property
    def username(self):
        return self.get_username()
