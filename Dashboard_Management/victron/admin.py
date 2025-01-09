from django.contrib import admin
from .models import VictronCredentials, VictronSite

admin.site.register(VictronSite)
@admin.register(VictronCredentials)
class VictronCredentialsAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'created_at')