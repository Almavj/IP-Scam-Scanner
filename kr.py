import requests

def korea():
    ip = input("Enter IP address to track in Korea: ")
    try:
        response = requests.get(f"https://ip-api.com/json/{ip}")
        data = response.json()

        print("\n[ IP Info - Korea ]")
        print(f"IP: {data.get('query')}")
        print(f"Country: {data.get('country')}")
        print(f"Region: {data.get('regionName')}")
        print(f"City: {data.get('city')}")
        print(f"ISP: {data.get('isp')}")
        print(f"Latitude: {data.get('lat')}")
        print(f"Longitude: {data.get('lon')}")
        print(f"Timezone: {data.get('timezone')}")
    except Exception as e:
        print(f"Error: {e}")
