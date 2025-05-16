from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any extra fields you want (e.g., student ID, etc.)
    student_id = models.CharField(max_length=20, blank=True) # Optional field
    def __str__(self):
        return self.username