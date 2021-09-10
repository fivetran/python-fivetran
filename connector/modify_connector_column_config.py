import requests
import environ
from requests.auth import HTTPBasicAuth

def modify_connector_column_config():

    env = environ.Env()
    environ.Env.read_env()

    # Adjust the payload settings to
    # reflect your settings from the
    # documentation.
    #
    # https://fivetran.com/docs/rest-api
    #
    # You need to insert your values next
    # to the appropiate key.
    # toggle these values for your spec.
    connector_id = ''
    schema_name = ''
    table_name = ''
    column_name = ''


    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/connectors/{}/schemas/{}/tables/{}/columns/{}'.format(connector_id, schema_name, table_name, column_name)

    # Adjust the payload settings to
    # reflect your settings from the
    # documentation.
    #
    # You need to insert your values next
    # to the appropiate key.
    payload = {
        "enabled": True,
        "hashed": False
    }
    
    request = requests.patch(url=endpoint, auth=base64, json=payload).json()
    print(request)