import re
import requests
import environ
from requests.auth import HTTPBasicAuth

def delete_group():

    env = environ.Env()
    environ.Env.read_env()

    # your group ID
    group_id = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/groups/{}'.format(group_id)

    request = requests.delete(url=endpoint, auth=base64).json()
    
    return request