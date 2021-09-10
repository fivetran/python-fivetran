import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def modify_destination():

    env = environ.Env()
    environ.Env.read_env()

    # your destination ID
    destination_id = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/destinations/{}'.format(destination_id)

    # toggle these values for your spec.
    # adjust payload according to the docs here:
    # https://fivetran.com/docs/rest-api
    #
    # Note that your payload values should differ
    # from existing values to sync a change.
    payload = {
        "region": "YOUR_REGION",
        "time_zone_offset": "+10",
        "config":{
            "host":"GET_FROM_YOUR_DESTINATION_SETUP",
            "port": 1433,
            "database": "DATABASE_NAME",
            "user": "USERNAME",
            "password": "PASSWORD"
        }
    }

    request = requests.patch(url=endpoint, auth=base64, json=payload).json()
    print(request)