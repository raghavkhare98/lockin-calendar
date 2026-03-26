from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import date

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
    lockin_activities = models.CharField(max_length=128, default="")
    user_photo = models.ImageField(upload_to="uploads/", null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = LockinUserManager

    @property
    def username(self):
        return self.get_username()

class LockinActivity(models.Model):
    activity_username = models.ForeignKey(LockinUser, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=128, null=False)
    activity_duration = models.DateField(default=date.today, null=False)
    activity_description = models.CharField(max_length=256, blank=True)
    activity_start_date = models.DateField(default=date.today, null=False)
    #have to generate activity_end_date automatically. Meaning that it should be a calculated field
    activity_completion_reward = models.CharField(max_length=128, blank=True)

class LockinActivityNotes(models.Model):
    note_text = models.TextField()
    note_activity_id = models.ForeignKey(LockinActivity, on_delete=models.CASCADE)
    created_at = models.DateField(unique=True)