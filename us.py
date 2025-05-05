import requests

def united_states():
    ip = input("Enter IP address to track in United States: ")
    try:
        # Add headers and verify response
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(
            f"http://ip-api.com/json/{ip}",
            headers=headers,
            timeout=10
        )
        data = response.json()
        
        # Check API status first
        if data.get('status') != 'success':
            error_msg = data.get('message', 'Unknown error')
            print(f"\n{Colors.RED}API Error: {error_msg}{Colors.RESET}")
            return
            
        print("\n[ IP Info - United States ]")
        print(f"IP: {data.get('query', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Region: {data.get('regionName', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"ISP: {data.get('isp', 'N/A')}")
        print(f"Latitude: {data.get('lat', 'N/A')}")
        print(f"Longitude: {data.get('lon', 'N/A')}")
        print(f"Timezone: {data.get('timezone', 'N/A')}")
        
    except requests.exceptions.RequestException as e:
        print(f"\n{Colors.RED}Network Error: {e}{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.RESET}")