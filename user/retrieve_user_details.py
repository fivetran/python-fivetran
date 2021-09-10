import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def retrieve_user_details():

    env = environ.Env()
    environ.Env.read_env()

    # your user ID
    user_id = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/users/{}'.format(user_id)

    request = requests.get(url=endpoint, auth=base64).json()
    print(json.dumps(request))