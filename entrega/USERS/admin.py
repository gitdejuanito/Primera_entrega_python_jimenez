from django.contrib import admin
from USERS.models import UserProfile
# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=("user","profile_picture","birth_Date")