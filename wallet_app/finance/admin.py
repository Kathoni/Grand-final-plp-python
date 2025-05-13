from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Transaction, Budget, Goal

admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(Goal)
