import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def retrieve_connector_schema():

    env = environ.Env()
    environ.Env.read_env()

    # your connector ID
    connector_id = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/connectors/{}/schemas'.format(connector_id)

    request = requests.get(url=endpoint, auth=base64).json()
    
    return request