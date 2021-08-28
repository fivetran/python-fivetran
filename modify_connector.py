import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def modify_connector():

    env = environ.Env()
    environ.Env.read_env()

    # your connector ID
    connector_id = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/connectors/{}'.format(connector_id)

    # Adjust the payload settings to
    # reflect your settings from the
    # documentation.
    #
    # https://fivetran.com/docs/rest-api
    #
    # You need to insert your values next
    # to the appropiate key.
    # toggle these values for your spec.
    payload = {
        "paused": False,
        "is_historical_sync": False,
        "sync_frequency": 30,
        "trust_certificate": True,
        "run_setup_tests": True,
        "config": {
            "username": "username",
            "password": "password"
        },
        "schedule_type": "manual"
    }

    request = requests.patch(url=endpoint, auth=base64, json=payload).json()
    print(request)