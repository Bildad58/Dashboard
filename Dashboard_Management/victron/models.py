from django.db import models
from dashboard.models import Sites


class VictronSite(models.Model):
    site = models.OneToOneField(Sites, on_delete=models.CASCADE)
    installation_id = models.CharField(max_length=100)
    last_sync = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Victron Integration for {self.site.Name}"

class VictronCredentials(models.Model):
    api_key = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Victron Credentials"