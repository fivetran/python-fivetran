import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def reload_connector_schema():

    env = environ.Env()
    environ.Env.read_env()

    # your connector ID
    connector_id = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/connectors/{}/schemas/reload'.format(connector_id)

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
        "exclude_mode": "PRESERVE"
    }

    request = requests.patch(url=endpoint, auth=base64, json=payload).json()
    print(request)