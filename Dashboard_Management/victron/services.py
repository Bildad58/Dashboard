# victron/services.py
import requests
from datetime import datetime, timedelta
from django.conf import settings
import json

class VictronAPI:
    BASE_URL = "https://vrmapi.victronenergy.com/v2"
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'X-Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def get_installation_data(self, installation_id):
        """Get current data for a specific installation"""
        endpoint = f"/installations/{installation_id}"
        return self._make_request('GET', endpoint)
    
    def get_site_stats(self, installation_id, start_time=None, end_time=None):
        """Get statistics for a specific time period"""
        if not start_time:
            start_time = (datetime.now() - timedelta(days=1)).isoformat()
        if not end_time:
            end_time = datetime.now().isoformat()
            
        endpoint = f"/installations/{installation_id}/stats"
        params = {
            'start': start_time,
            'end': end_time
        }
        return self._make_request('GET', endpoint, params=params)
    
    def _make_request(self, method, endpoint, params=None, data=None):
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.request(
                method,
                url,
                headers=self.headers,
                params=params,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request to Victron API: {str(e)}")
            return None