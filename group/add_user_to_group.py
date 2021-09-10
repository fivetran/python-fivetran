import requests
import environ
from requests.auth import HTTPBasicAuth

def add_user_to_group():

    env = environ.Env()
    environ.Env.read_env()

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    # your group ID
    group_id = ''

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/groups/{}/users'.format(group_id)

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
        'email': 'YOUR_EMAIL',
        'role': 'Admin'
    }

    response = requests.post(url=endpoint, auth=base64, json=payload).json()
    print(response)