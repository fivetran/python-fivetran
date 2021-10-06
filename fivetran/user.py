import requests
from fivetran.fivetranapi import FivetranApi, _url_builder, BASE_ENDPOINT, USERS_ENDPOINT, _param_builder

class User(FivetranApi):
  def __init__(self, apiKey=None, apiSecret=None, version=None, debug=False):
    super().__init__(
      apiKey=apiKey, 
      apiSecret=apiSecret, 
      version=version, 
      debug=debug
    )

    self._url = _url_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      USERS_ENDPOINT
    )
    
  
  def invite(self, email: str, givenName: str, familyName: str, role: str, phone: str= None, picture: str = None) -> dict:
    payload = {
      "email": email,
      "give_name": giveName,
      "family_name": familyName
    }

    if phone is not None:
      payload['phone'] = phone

    if picture is not None:
      payload['picture'] = picture

    r = self._post(
      endpoint
      payload
    )

    self.debug(r)

    return r