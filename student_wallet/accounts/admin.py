from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'student_id']  # Customize admin display
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('student_id',)}),  # Add custom fields to admin
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('student_id',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)