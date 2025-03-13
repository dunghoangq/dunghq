import requests
import pandas as pd
import numpy as np

# f0d7a8c9503e4ca78f3bd8dbf37ac4a6414e8b2a
CLIENT_ID = 'f0d7a8c9503e4ca78f3bd8dbf37ac4a6414e8b2a'
USERNAME = 'dungqhoang@deloitte.com'
PASSWORD = 'Dung@1102'

url = "https://api.refinitiv.com/auth/oauth2/v1/token"

auth_payload = {
    "grant_type": "password",
    "username": USERNAME,
    "password": PASSWORD,
    "client_id": CLIENT_ID,
    "scope": "trapi",
}

auth_response = requests.post(url, data=auth_payload)

if auth_response.status_code == 200:
    access_token = auth_response.json().get("access_token")
    print("Authentication successful!")
else:
    print("Failed to authenticate:", auth_response.json())
