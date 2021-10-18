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
      "given_name": giveName,
      "family_name": familyName,
      "role": role
    }

    if phone is not None:
      payload['phone'] = phone

    if picture is not None:
      payload['picture'] = picture

    r = self._post(
      self.getUrl(),
      payload
    )

    self.debug(r)

    return r

  def list(self, cursor: str = None, limit: int = 100) -> dict:
    param_dict = {
      "limit": limit,
      "cursor": cursor

    }
    query_params = _param_builder(param_dict)

    endpoint = _url_builder(
      self.getUrl(),
      _query_params=query_params
    )

    r = self._get(
      endpoint
    )

    return r

  def listAll(self) -> dict:
    r = self._iterator(
      self.list
    )

    return r

  def getDetails(self, userId: str):
    endpoint = _url_builder(
      self.getUrl(),
      _id=userId
    )

    r = self._get(
      endpoint
    )

    return r

  def modify(self, userId: str, givenName: str = None, 
    familyName: str = None, role: str = None, phone: str= None, 
    picture: str = None
  ) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=userId
    )

    payload = {}

    if givenName is not None:
      payload['given_name'] = givenName

    if familyName is not None:
      payload['family_name'] = familyName

    if role is not None:
      payload['role'] = role

    if phone is not None:
      payload['phone'] = phone

    if picture is not None:
      payload['picture'] = picture

    r = self._patch(
      endpoint,
      payload
    )

    self.debug(r)

    return r

  def delete(self, userId: str) -> dict:
    endpoint = _url_builder(
      self.getUrl,
      _id=userId
    )

    r = self._delete(
      endpoint
    )

    self.debug(r)

    return r

  def deleteBulk(self, userIds: list) -> dict:
    results = {}
    for userId in userIds:
      r = self._delete(
        userId
      )

      results[userId] = r

    return results

if __name__ == '__main__':
  u = User(debug=True)

  u.list()

  u.getDetails('competence_elucidation')









