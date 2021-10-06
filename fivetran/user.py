import requests
from fivetran.fivetranapi import FivetranApi, _uri_builder, BASE_ENDPOINT, USERS_ENDPOINT

class User(FivetranApi):
  def __init__(self, apiKey=None, apiSecret=None, version=None, debug=False):
    super().__init__(
      apiKey=apiKey, 
      apiSecret=apiSecret, 
      version=version, 
      debug=debug
    )
    
  
  def invite(self, email, givenName, familyName, role, phone=None, picture=None):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      USERS_ENDPOINT
    )

    payload = {
      "email": email,
      "give_name": giveName
    }

    if phone is not None:
      payload['phone'] = phone


    r = requests.post(
      endpoint,
      auth=self.getAuth(),
      json=payload
    ).json()

    self.debug(r)

    return r