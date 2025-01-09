import requests
import sys

class VRMTester:
    def __init__(self):
        self.base_url = "https://vrmapi.victronenergy.com/v2/"
        
    def test_connection(self):
        """Test basic connectivity to VRM"""
        try:
            response = requests.get(self.base_url + 'installations', timeout=10)
            print(f"HTTP Status: {response.status_code}")
            print(f"Response Content: {response.text[:200]}...")  # First 200 chars
            print(f"Basic connection test: {'Success' if response.ok else 'Failed'}")
            return response.ok
        except requests.exceptions.RequestException as e:
            print(f"Connection error: {e}")
            return False

    def test_auth(self, token):
        """Test authentication with token"""
        headers = {
            'X-Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.get(f"{self.base_url}installations", headers=headers, timeout=10)
            print(f"Response Status: {response.status_code}")
            print(f"Response: {response.text[:200]}...")  # First 200 chars
            
            if response.status_code == 401:
                print("Authentication failed. Verify your token.")
            
            return response.ok
        except requests.exceptions.RequestException as e:
            print(f"Authentication error: {e}")
            return False

def main():
    print("VRM Portal Access Tester")
    print("=======================")
    
    tester = VRMTester()
    
    # Test basic connectivity
    if not tester.test_connection():
        print("Cannot connect to VRM Portal. Check your internet connection or API endpoint.")
        sys.exit(1)
    
    # Get token from user
    token = input("\nf5f7b410347129df703b897698cf210ddc14b4be54fe21cb4fde473d7ec84d59: ").strip()
    
    # Test authentication
    tester.test_auth(token)

if __name__ == "__main__":
    main()
