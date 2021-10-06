import json
import requests
import environ
from requests.auth import HTTPBasicAuth

def list_all_users_in_group():

    env = environ.Env()
    environ.Env.read_env()

    # your group ID
    group_id = ''

    limit = 1000
    pagination = {"limit": limit}

    API_KEY = env("API_KEY")
    API_SECRET = env("API_SECRET")

    base64 = HTTPBasicAuth(API_KEY, API_SECRET)
    endpoint = "https://api.fivetran.com/v1/groups/{}/users".format(group_id)

    request = requests.get(url=endpoint, auth=base64, params=pagination).json()
    users_list = request["data"]["items"]

    while "next_cursor" in response["data"]:
        print("paged")

        params = {"limit": pagination, "cursor": request["data"]["next_cursor"]}
        response_paged = requests.get(url=endpoint, auth=base64, params=params).json()
        
        if any(response_paged["data"]["items"]) == True:
            users_list.extend(response_paged["data"]["items"])
        response = response_paged

    return users_list