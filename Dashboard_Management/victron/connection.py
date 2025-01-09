import requests

def get_installations(token):
    """Fetch all installations for the authenticated user."""
    url = "https://vrmapi.victronenergy.com/v2/installations"
    headers = {
        'X-Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.ok:
            installations = response.json().get('records', [])
            print("Available Installations:")
            for install in installations:
                print(f"- ID: {install['idSite']}, Name: {install['name']}")
            return installations
        else:
            print("Failed to fetch installations. Check your token or account.")
            print("Response:", response.status_code, response.text)
    except Exception as e:
        print(f"Error fetching installations: {e}")

# Example usage:
token = input("f5f7b410347129df703b897698cf210ddc14b4be54fe21cb4fde473d7ec84d59: ").strip()
get_installations(token)
