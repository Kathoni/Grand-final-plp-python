from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    budget_limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()  # Consider using DateTimeField if needed

    def __str__(self):
        return f"{self.description} - {self.amount}"