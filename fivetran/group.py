import requests

from fivetran.fivetranapi import FivetranApi, _uri_builder, BASE_ENDPOINT, GROUPS_ENDPOINT

class Group(FivetranApi):
  def __init__(self, apiKey=None, apiSecret=None, version=None, debug=False):
    super().__init__(
      apiKey=apiKey, 
      apiSecret=apiSecret, 
      version=version, 
      debug=debug
    )
    
  
  def create(self, name: str) -> dict:
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      GROUPS_ENDPOINT
    )

    payload = {
      "name": name
    }

    r = requests.post(
      endpoint,
      auth=self.getAuth(),
      json=payload
    ).json()

    self.debug(r)

    return r

  def list(self, cursor=None, limit=100):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      GROUPS_ENDPOINT
    )

    endpoint = "{}?limit={}".format(
      endpoint,
      limit
    )

    if cursor is not None:
      endpoint = "{}&cursor={}".format(
        endpoint,
        cursor
      )

    r = requests.get(
      endpoint,
      auth=self.getAuth()
    ).json()

    self.debug(r)

    return r

  def listAll(self):
    '''example of an how an SDK can provide more value by writing
    helper functions for common operations.
    e.g., I want to list all the groups without having 
    to paginate myself'''

    #default cursor
    cursor = None

    #get first page
    r = self.list(
      cursor=cursor,
      limit=1000
    )

    #check if we're done, if False, we skip the while loop
    cursorExists = 'next_cursor' in r['data'].keys()

    #if the cursor exists then set it as the new cursor
    if cursorExists:
      cursor = r['data']['next_cursor']

    while cursorExists:
      #we have a new cursor so get get next page and so on
      tmp = self.list(
        cursor=cursor,
        limit=1000
      )
      
      #add the new items to the first page
      r['data']['items'].extend(
        tmp['data']['items']
      )

      #check if we're done, if not set the new cursor
      cursorExists = 'next_cursor' in tmp['data'].keys()
      if cursorExists:
        cursor = tmp['data']['next_cursor']

    return r

  def getDetails(self, groupId):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      GROUPS_ENDPOINT,
      _id=groupId
    )

    r = requests.get(
      endpoint,
      auth=self.getAuth()
    ).json()

    self.debug(r)

    return r

  def modify(self, groupId, name):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      GROUPS_ENDPOINT,
      _id=groupId
    )

    payload = {
      "name": name
    }

    r = requests.patch(
      endpoint,
      auth=self.getAuth(),
      json=payload
    ).json()

    self.debug(r)

    return r

  def listConnectors(self, groupId, cursor=None, limit=100, schema=None):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      GROUPS_ENDPOINT,
      _id=groupId,
      _params='connectors'
    )

    endpoint = "{}?limit={}".format(
      endpoint,
      limit
    )

    if schema is not None:
      endpoint = "{}&schema={}".format(
        endpoint,
        schema
      )

    if cursor is not None:
      endpoint = "{}&cursor={}".format(
        endpoint,
        cursor
      )

    r = requests.get(
      endpoint,
      auth=self.getAuth()
    ).json()

    self.debug(r)
    print(endpoint)

    return r

  def listAllConnectors(self, groupId, schema=None):
    pass

  def listUsers(self, groupId, cursor=None, limit=100):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      GROUPS_ENDPOINT,
      _id=groupId,
      _params='users'
    )

    endpoint = "{}?limit={}".format(
      endpoint,
      limit
    )

    if cursor is not None:
      endpoint = "{}&cursor={}".format(
        endpoint,
        cursor
      )

    r = requests.get(
      endpoint,
      auth=self.getAuth()
    ).json()

    self.debug(r)

    return r

  def listAllUsers(self, groupId):
    pass

  def addUser(self, groupId, email, role):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      GROUPS_ENDPOINT,
      _id=groupId,
      _params='users'
    )

    payload = {
      "email": email,
      "role": role
    }

    r = requests.get(
      endpoint,
      auth=self.getAuth(),
      json=payload
    ).json()

    self.debug(r)

    return r    


  def removeUser(self, groupId, userId):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      GROUPS_ENDPOINT,
      _id=groupId,
      _params='users/{}'.format(
        userId
      )
    )

    r = requests.delete(
      endpoint,
      auth=self.getAuth()
    ).json()

    self.debug(r)

    return r

  def removeUsers(self, groupId, userIds):
    results = []
    for userId in userIds:
      r = self.removeUser(
        groupId, 
        userId
      )

      results.append(r)

    return results

  def delete(self, groupId):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      GROUPS_ENDPOINT,
      _id=groupId
    )

    r = requests.delete(
      endpoint,
      auth=self.getAuth()
    ).json()

    self.debug(r)

    return r


if __name__ == '__main__':
  g = Group(
    debug=True
  )

  r = g.create('TypeTest')



    