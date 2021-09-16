import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def delete_destination():

    env = environ.Env()
    environ.Env.read_env()

    # your destination ID
    destination_id = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/destinations/{}'.format(destination_id)

    request = requests.delete(url=endpoint, auth=base64).json()
    
    return request