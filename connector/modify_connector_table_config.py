import requests
import environ
from requests.auth import HTTPBasicAuth

def modify_connector_config():

    env = environ.Env()
    environ.Env.read_env()

    # your connector ID
    connector_id = ''
    schema = ''
    table = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/connectors/{}/schemas/{}/tables/{}'.format(connector_id, schema, table)

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
        "enabled": False,
        "columns": {
            "COLUMN_NAME": {
                "enabled": True,
                "hashed": False
            },
            "COLUMN_NAME": {
                "hashed": True
            }
        }
    }

    request = requests.patch(url=endpoint, auth=base64, json=payload).json()
    
    return request