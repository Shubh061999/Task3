
import requests
import json

api_url = "http://api.apis.guru/v2/list.json"

try:
    response = requests.get(api_url)
    response.raise_for_status()

    if response.status_code == 200:
        data = response.text
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")


