# victron/views.py
from django.shortcuts import render
from django.contrib import messages
from .models import VictronSite, VictronCredentials
from .services import VictronAPI
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def sync_victron_data(request, site_id):
    try:
        victron_site = VictronSite.objects.get(site_id=site_id)
        credentials = VictronCredentials.objects.filter(is_active=True).first()
        
        if not credentials:
            messages.error(request, "No active Victron API credentials found")
            return redirect('dashboard')
            
        api = VictronAPI(credentials.api_key)
        installation_data = api.get_installation_data(victron_site.installation_id)
        
        if installation_data:
            # Update site status based on Victron data
            site = victron_site.site
            site.status = 'Online' if installation_data.get('connection', False) else 'Offline'
            
            # Update other relevant site data
            if 'extended' in installation_data:
                ext_data = installation_data['extended']
                site.Size = f"{ext_data.get('pvPowerPeak', 0)} kW"
                site.Load = f"{ext_data.get('acload', 0)} kW"
            
            site.save()
            messages.success(request, f"Successfully synced data for {site.Name}")
        else:
            messages.warning(request, f"No data received from Victron API for {victron_site.site.Name}")
            
    except VictronSite.DoesNotExist:
        messages.error(request, "Victron integration not found for this site")
    except Exception as e:
        messages.error(request, f"Error syncing Victron data: {str(e)}")
    
    return redirect('dashboard')