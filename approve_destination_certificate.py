import requests
import environ
from requests.auth import HTTPBasicAuth

def approve_destination_cert():

    env = environ.Env()
    environ.Env.read_env()

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/certificates'

    # Adjust the payload settings to
    # reflect your settings from the
    # documentation.
    #
    # You need to insert your values next
    # to the appropiate key.

    payload = {
        'connector_id': 'YOUR_CONNECTOR_ID',
        'hash': 'YOUR_CERT_HASH',
        'encoded_cert': 'YOUR_BASE64_CERT'
    }

    response = requests.post(url=endpoint, auth=base64, json=payload).json()
    print(response)