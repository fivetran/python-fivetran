import requests
from fivetranapi import FivetranApi, _uri_builder, BASE_ENDPOINT, GROUPS_ENDPOINT

class Group(FivetranApi):
  def __init__(self, apiKey=None, apiSecret=None, version=None, debug=False):
    super().__init__(
      apiKey=apiKey, 
      apiSecret=apiSecret, 
      version=version, 
      debug=debug
    )
    
  
  def create(self, name):
    endpoint = fivetranapi._uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      GROUPS_ENDPOINT
    )

    payload = {
      "name": name
    }

    r = requests.post(
      endpoint,
      auth=self._auth,
      json=payload
    ).json()

    self.debug(r)

    return r

  

    