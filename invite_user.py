import requests
import environ
from requests.auth import HTTPBasicAuth

def invite_user():

    env = environ.Env()
    environ.Env.read_env()

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/users'
    
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
        'given_name': 'FIRST_NAME', # enter the first name
        'family_name': 'LAST_NAME', # enter the last name
        'email': 'USER@DOMAIN.COM', # enter the email address
        'role': 'Owner' # enter the role from option of 'ReadOnly' or 'Owner'
    }

    response = requests.post(url=endpoint, auth=base64, json=payload).json()
    print(response)