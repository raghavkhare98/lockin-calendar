from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import date

class LockinUserManager(BaseUserManager):
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        return self._create_user(email, password, **extra_fields)

class LockinUser(AbstractUser):
    email = models.EmailField(unique=True)
    lockin_activities = models.CharField(max_length=128, default="")
    date_joined = models.DateTimeField(auto_now_add=True)
    user_photo = models.ImageField(upload_to="uploads/", null=True, blank=True)

    objects = LockinUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def username(self):
        return self.get_username()

class LockinActivity(models.Model):
    user = models.ForeignKey(LockinUser, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=128)
    activity_end_date = models.DateField() #renamed end_date because duration is wrong english, removed default today because the activity would expire immediately after creation
    activity_description = models.CharField(max_length=256, blank=True)
    activity_start_date = models.DateField(default=date.today)
    activity_completion_reward = models.CharField(max_length=128, blank=True)

class LockinActivityNotes(models.Model):
    note_text = models.TextField()
    activity = models.ForeignKey(LockinActivity, on_delete=models.CASCADE)
    created_at = models.DateField()

    class Meta:
        unique_together = [('activity', 'created_at')] #did this because created_at unique=True wouldn't have enabled more than 1 user to add a note (even in different accounts)