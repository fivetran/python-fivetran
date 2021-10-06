import requests
import environ
from requests.api import request
from requests.auth import HTTPBasicAuth

def approve_connector_fingerprint():

    env = environ.Env()
    environ.Env.read_env()

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/fingerprints'

    # Adjust the payload settings to
    # reflect your settings from the
    # documentation.
    #
    # You need to insert your values next
    # to the appropiate key.

    payload = {
        'connector_id': 'YOUR_CONNECTOR',
        'hash': 'YOUR_HASH',
        'public_key': 'YOUR_PUBLIC_KEY'
    }

    request = requests.post(url=endpoint, auth=base64, json=payload).json()
    
    return request