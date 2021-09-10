import requests
import environ
from requests.auth import HTTPBasicAuth

def run_connector_setup_tests():

    env = environ.Env()
    environ.Env.read_env()

    # your connector ID
    connector_id = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = 'https://api.fivetran.com/v1/connectors/{}/test'.format(connector_id)

    # toggle these values for your spec.
    # adjust payload according to the docs here:
    # https://fivetran.com/docs/rest-api
    #
    # Note that your payload values should differ
    # from existing values to sync a change.
    payload = {
        "trust_certificates": True,
        "trust_fingerprints": True
    }

    request = requests.post(url=endpoint, auth=base64, json=payload).json()
    print(request)