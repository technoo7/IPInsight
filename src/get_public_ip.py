import requests
from exceptions import RequestError, IPDetailsError

# Fetch Public IP
def get_public_ip():
    try:
        response = requests.get("https://ipinfo.io")
        if response.status_code == 200:
            data = response.json()
            return data.get('ip')
        else:
            print("Unable to retrieve IP address.")
    except requests.exceptions.RequestException as e:
        raise RequestError("Failed to retrieve public IP")
        print("Hint: Check Your Internet")
    except json.JSONDecodeError as e:
        raise IPDetailsError("Failed to parse JSON response")