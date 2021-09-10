import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def list_connectors_in_group():

    env = environ.Env()
    environ.Env.read_env()

    limit = 1000
    pagination = {"limit": limit}

    # your connector ID
    connector_id = ''

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = "https://api.fivetran.com/v1/groups/{}/connectors".format(connector_id)

    request = requests.get(url=endpoint, auth=base64, params=pagination).json()
    connectors_list = request["data"]["items"]

    while "next_cursor" in response["data"]:
        print("paged")

        params = {"limit": pagination, "cursor": request["data"]["next_cursor"]}

        response_paged = requests.get(url=endpoint, auth=base64, params=params).json()
        
        if any(response_paged["data"]["items"]) == True:
            connectors_list.extend(response_paged["data"]['items'])
        response = response_paged

print(json.dumps(connectors_list))