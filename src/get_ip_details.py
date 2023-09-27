import requests
import socket
import json

from exceptions import IPDetailsError, GeolocationError

# Get IP Details
def get_ip_details(ip):
    try:
        # Get geolocation information using a free IP geolocation API (ipinfo.io)
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        geolocation_data = json.loads(response.text)

        # Display the gathered information
        print(f"IP Address: {ip}")
        print(f"Hostname: {geolocation_data.get('hostname', 'Not found')}")
        print(f"Location: {geolocation_data.get('loc', 'Not found')}")
        print(f"City: {geolocation_data.get('city', 'Not found')}")
        print(f"Region: {geolocation_data.get('region', 'Not found')}")
        print(f"Country: {geolocation_data.get('country', 'Not found')}")
        print(f"Provider: {geolocation_data.get('org', 'Not found')}")
        print(f"Timezone: {geolocation_data.get('timezone', 'Not found')}")
        print(f"Postal: {geolocation_data.get('postal', 'Not found')}")  
    except socket.herror:
        raise IPDetailsError("Invalid, unreachable, or private IP address. Try Again with Public IP")
    except requests.exceptions.RequestException as e:
        raise GeolocationError("Failed to retrieve geolocation information.")
    except json.JSONDecodeError as e:
        raise IPDetailsError("Failed to parse JSON response.")