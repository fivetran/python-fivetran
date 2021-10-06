import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def retrieve_source_metadata():

    env = environ.Env()
    environ.Env.read_env()

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/metadata/connectors'

    request = requests.get(url=endpoint, auth=base64).json()
    
    return request