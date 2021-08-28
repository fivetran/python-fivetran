import requests
import environ
from requests.auth import HTTPBasicAuth

def create_connector():

    env = environ.Env()
    environ.Env.read_env()

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/connectors'

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
        'service': 'YOUR_SERVICE_NAME',
        'group_id': 'YOUR_GROUP_ID',
        'trust_certificates': True,
        'run_setup_tests': True,
        'config': {
            'schema': 'YOUR_NAMED_SCHEMA'
        }
    }

    response = requests.post(url=endpoint, auth=base64, json=payload).json()
    print(response)