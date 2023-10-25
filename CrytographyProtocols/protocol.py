import requests
import certifi

url = "https://google.com"

ca_bundle = certifi.where()

try:
    response = requests.get(url, verify=ca_bundle)

    if response.status_code == 200:
        print("Request was successful.")
        print("Response content:")
        print(response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.SSLError as e:
    print(f"SSL error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
