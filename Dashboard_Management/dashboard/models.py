from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.cache import cache
from django.db import models

class SystemStatus(models.Model):
    STATUS_CHOICES = [
        ('normal', 'Normal'),
        ('warning', 'Warning'),
        ('alarm', 'Alarm'),
    ]

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "System Statuses"

    def __str__(self):
        return f"{self.name} - {self.status}"

        
class Sites(models.Model):
    STATUS_CHOICES = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    ]

    Name = models.CharField(max_length=100)
    Size = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Load = models.CharField(max_length=100)

    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='Online',  # Default value
    )
    is_deleted = models.BooleanField(default=False)
    Commissioned = models.DateField(auto_now_add=True, blank=False)

    @classmethod
    def get_lifetime_capacity(cls):
        return cache.get('lifetime_capacity', 0)

    @classmethod
    def update_lifetime_capacity(cls, size_to_add):
        current_total = cls.get_lifetime_capacity()
        new_total = current_total + size_to_add
        cache.set('lifetime_capacity', new_total, None)
        return new_total
    
    def __str__(self):
        return self.Name
    
class Assets(models.Model):
    Installed_capacity = models.CharField(max_length=100)
    Energy_generated = models.CharField(max_length=100)



