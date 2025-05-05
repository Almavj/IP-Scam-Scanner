import requests

def indonesia():
    ip = input("Enter IP address to track in Indonesia: ")
    try:
        response = requests.get(f"https://ip-api.com/json/{ip}")
        data = response.json()

        print("\n[ IP Info - Indonesia ]")
        print(f"IP: {data.get('query')}")
        print(f"Country: {data.get('country')}")
        print(f"Region: {data.get('regionName')}")
        print(f"City: {data.get('city')}")
        print(f"ISP: {data.get('isp')}")
        print(f"Latitude: {data.get('lat')}")
        print(f"Longitude: {data.get('lon')}")
        print(f"Timezone: {data.get('timezone')}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print("Failed to retrieve IP information. Check your network connection and the IP address.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please check the IP address and try again.")

if __name__ == "__main__":
    indonesia()  # added for testing
