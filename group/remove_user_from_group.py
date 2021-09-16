import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def remove_user_from_group():

    env = environ.Env()
    environ.Env.read_env()

    # your group and user ID
    group_id = ''
    user_id = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/groups/{}/users/{}'.format(group_id, user_id)

    request = requests.delete(url=endpoint, auth=base64).json()

    return request