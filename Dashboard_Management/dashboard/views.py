from django.shortcuts import render
from .models import *
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Sum
import re
from django.db.models import Count
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from victron.models import VictronCredentials


@login_required
def SITE(request):
    sites = Sites.objects.all()
    context = {
        'sites': sites
    }
    return render(request, 'dashboard/site.html', context)

def parse_size_to_kw(size_str):
    """Convert size string with units to kW numeric value"""
    try:
        match = re.match(r'(\d+(?:\.\d+)?)\s*(kW|MW|GW)?', str(size_str), re.IGNORECASE)
        if not match:
            return 0
        
        number, unit = match.groups()
        number = float(number)
        
        if unit:
            unit = unit.upper()
            if unit == 'MW':
                number *= 1000
            elif unit == 'GW':
                number *= 1000000
        
        return number
    except (ValueError, AttributeError):
        return 0
@login_required
def site_add(request):
    if request.method == 'POST':
        new_size = parse_size_to_kw(request.POST['size'])
        
        site = Sites.objects.create(
            Name=request.POST['name'],
            Size=request.POST['size'],
            Location=request.POST['location'],
            Load=request.POST['load'],
            status=request.POST['status']
        )
        
        Sites.update_lifetime_capacity(new_size)  # Call the class method
        return redirect('site')
    return redirect('site')
@login_required
def site_edit(request, pk):
    site = get_object_or_404(Sites, pk=pk)
    if request.method == 'POST':
        site.Name = request.POST['name']
        site.Size = request.POST['size']
        site.Location = request.POST['location']
        site.Load = request.POST['load']
        site.status = request.POST['status']
        site.save()
        return redirect('site')
    return redirect('site')


def site_delete(request, pk):
    site = Sites.objects.get(pk=pk)
    site.delete()  # This will now set is_deleted to True instead of actually deleting
    return redirect('site')


@login_required
def Dashboard(request): 
    sites = Sites.objects.all()
    online_count = Sites.objects.filter(status='Online').count()
    offline_count = Sites.objects.filter(status='Offline').count()
    active_sites = Sites.objects.filter(is_deleted=False)
     # Get all non-deleted sites
    active_sites = Sites.objects.filter(is_deleted=False)
    
    # Calculate current capacity
    current_total_kw = sum(parse_size_to_kw(site.Size) for site in active_sites)
    
    # Get lifetime capacity
    lifetime_total_kw = Sites.get_lifetime_capacity()
    VictronCredentials.objects.all()
    
    # Format for display
    def format_capacity(kw_value):
        if kw_value >= 1000000:
            return f"{kw_value/1000000:.1f} GW"
        elif kw_value >= 1000:
            return f"{kw_value/1000:.1f} MW"
        else:
            return f"{kw_value:.1f} kW"

     # Calculate total current capacity (from all active sites, both online and offline)
    
   
    context = {
        
        'sites': sites,
        'online_count': online_count,
        'offline_count': offline_count,
        'current_capacity': format_capacity(current_total_kw),
        'lifetime_capacity': format_capacity(lifetime_total_kw),
        'victron_api_key': VictronCredentials.objects.filter(is_active=True).first().api_key,

   
    }
    return render(request, 'dashboard/index.html', context)



#SYSTEM STATUS
def get_system_status_counts(request):
    # Get counts for each status
    status_counts = SystemStatus.objects.values('status').annotate(count=Count('status'))
    
    # Convert to dictionary format
    counts = {
        'normal': [],
        'warning': [],
        'alarm': [],
        'total': SystemStatus.objects.count()
    }
    
    for item in status_counts:
        counts[item['status']] = item['count']
    
    return JsonResponse(counts)

def system_status_view(request):
    return render(request, 'dashboard/alert_list.html')