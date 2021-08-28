import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def resync_connector_table():

    env = environ.Env()
    environ.Env.read_env()

    connector_id = ''
    schema = ''
    table = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/connectors/{}/schemas/{}/tables/{}/resync'.format(connector_id, schema, table)

    response = requests.post(url=endpoint, auth=base64).json()
    print(response)