import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def list_all_groups():

    env = environ.Env()
    environ.Env.read_env()
    
    limit = 1000
    pagination = {"limit": limit}

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = "https://api.fivetran.com/v1/groups"

    request = requests.get(url=endpoint, auth=base64, params=pagination).json()
    groups_list = request["data"]["items"]

    while "next_cursor" in response["data"]:
        print("paged")

        params = {"limit": pagination, "cursor": request["data"]["next_cursor"]}
        response_paged = requests.get(url=endpoint, auth=base64, params=params).json()
        
        if any(response_paged["data"]["items"]) == True:
            groups_list.extend(response_paged["data"]["items"])
        response = response_paged

    return groups_list