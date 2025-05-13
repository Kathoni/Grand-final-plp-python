from django.db import models

# Create your models here.
CATEGORY_CHOICES = [
    ('Food', 'Food'),
    ('Transport', 'Transport'),
    ('Rent', 'Rent'),
    ('Entertainment', 'Entertainment'),
    ('Education', 'Education'),
    ('Other', 'Other'),
]

class Transaction(models.Model):
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

class Budget(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    limit = models.DecimalField(max_digits=10, decimal_places=2)

class Goal(models.Model):
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_date = models.DateField()
