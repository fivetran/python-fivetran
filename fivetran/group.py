import requests

from fivetran.fivetranapi import FivetranApi, _url_builder, BASE_ENDPOINT, GROUPS_ENDPOINT, _param_builder

class Group(FivetranApi):
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
      GROUPS_ENDPOINT
    )
  
  def create(self, name: str) -> dict:
    payload = {
      "name": name
    }

    r = self._post(
      self.getUrl(),
      payload
    )

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

  def getDetails(self, groupId: str) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=groupId
    )

    r = self._get(
      endpoint
    )

    return r

  def modify(self, groupId: str, name: str) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=groupId
    )

    payload = {
      "name": name
    }

    r = self._patch(
      endpoint,
      json=payload
    )

    return r

  def listConnectors(self, groupId: str, cursor: str = None, limit: int = 100, schema: str = None) -> dict:
    param_dict = {
      "limit": limit,
      "cursor": cursor,
      "schema": schema

    }
    query_params = _param_builder(param_dict)

    endpoint = _url_builder(
      self.getUrl(),
      _id=groupId,
      _path='connectors',
      _query_params=query_params
    )

    r = self._get(
      endpoint
    )

    return r

  def listAllConnectors(self, groupId: str, schema: str = None) -> dict:
    r = self._iterator(
      self.listConnectors,
      groupId=groupId,
      schema=schema
    )

    return r

  def listUsers(self, groupId: str, cursor: str = None, limit: int = 100) -> dict:
    param_dict = {
      "limit": limit,
      "cursor": cursor
    }

    query_params = _param_builder(param_dict)

    endpoint = _url_builder(
      self.getUrl(),
      _id=groupId,
      _path='users',
      _query_params=query_params
    )

    r = self._get(
      endpoint
    )

    return r

  def listAllUsers(self, groupId: str) -> dict:
    r = self._iterator(
      self.listUsers,
      groupId=groupId,
      schema=schema
    )

    return r

  def addUser(self, groupId: str, email: str, role: str) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=groupId,
      _path='users'
    )

    payload = {
      "email": email,
      "role": role
    }

    r = self._post(
      endpoint,
      payload
    )

    return r    


  def removeUser(self, groupId: str, userId: str) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=groupId,
      _path='users/{}'.format(
        userId
      )
    )

    r = self._delete(
      endpoint
    )

    return r

  def removeUsers(self, groupId: str, userIds: list) -> dict:
    results = {}
    for userId in userIds:
      r = self.removeUser(
        groupId, 
        userId
      )

      results[userId] = r

    return results

  def delete(self, groupId: str) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=groupId
    )

    r = self._delete(
      endpoint
    )

    return r

  def deleteBulk(self, groupIds: list) -> dict:
    results = {}
    for groupId in groupIds:
      r = self._delete(
        groupId
      )

      results[groupId] = r

    return results


if __name__ == '__main__':
  g = Group(
    debug=True
  )

  r = g.listAll()

  g._print(r)

  print(len(r['response']['data']['items']))

  g.listUsers('photograph_scalp')



    