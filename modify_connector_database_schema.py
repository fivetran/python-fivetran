import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def modify_connector_database_schema():

    env = environ.Env()
    environ.Env.read_env()

    # your connector ID
    connector_id = ''

    # schema name for destination
    schema_name = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/connectors/{}/schemas/{}'.format(connector_id, schema_name)

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
        "enabled": True,
        "tables": {
            "table_1": {
                "enabled": True
            },
            "table_2": {
                "enabled": False,
                "columns": {
                    "column_2": {
                        "enabled": True,
                        "hashed": False
                    },
                    "column_3": {
                        "hashed": True
                    }
                }
            }
        }   
    }
    
    request = requests.patch(url=endpoint, auth=base64, json=payload).json()
    print(request)