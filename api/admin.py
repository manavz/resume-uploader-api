from django.contrib import admin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    _DisplayT = ['id', 'name', 'email', 'dob',
                 'state', 'gender', 'location', 'pimage', 'rdoc']

    list_display: _DisplayT
