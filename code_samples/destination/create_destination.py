import requests
import environ
from requests.api import request
from requests.auth import HTTPBasicAuth

def create_destination():

    env = environ.Env()
    environ.Env.read_env()

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/destinations'

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
        "group_id": "YOUR_GROUP_ID",
        "service": "SERVICE_NAME",
        "region": "US",
        "time_zone_offset": "-5",
        "config": {
            "host": "GET_THIS_FROM_YOUR_SERVICE",
            "port": 443,
            "database": "DB_NAME",
            "user": "USERNAME",
            "password": "USE_AN_ENVAR"
    }
}

    request = requests.post(url=endpoint, auth=base64, json=payload).json()
    
    return request