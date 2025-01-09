from . import views
from django.urls import path

# Add to urls.py
urlpatterns = [
    path('sync/', views.sync_victron_data, name='sync_victron_data'),
]