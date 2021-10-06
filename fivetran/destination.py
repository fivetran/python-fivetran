import requests

from fivetran.fivetranapi import FivetranApi, _uri_builder, BASE_ENDPOINT, DESTINATION_ENDPOINT

class Destination(FivetranApi):
  def __init__(self, apiKey=None, apiSecret=None, version=None, debug=False):
    super().__init__(
      apiKey=apiKey, 
      apiSecret=apiSecret, 
      version=version, 
      debug=debug
    )
  
  def create(self, group_id, service, time_zone_offset, config):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      DESTINATION_ENDPOINT
    )

    payload = {
      "group_id": group_id,
      "service": service,
      "time_zone_offset": time_zone_offset,
      "config": config
    }

    r = requests.post(
      endpoint,
      auth=self.getAuth(),
      json=payload
    ).json()

    self.debug(r)

    return r

  def getDetails(self, destinationId):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      DESTINATION_ENDPOINT,
      _id=destinationId
    )

    r = requests.get(
      endpoint,
      auth=self.getAuth()
    ).json()

    self.debug(r)

    return r

  def modify(self, destinationId, region, time_zone_offset, config):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      DESTINATION_ENDPOINT,
      _id=destinationId
    )

    payload = {
      "region": region,
      "time_zone_offset": time_zone_offset,
      "config": config
    }

    r = requests.patch(
      endpoint,
      auth=self.getAuth(),
      json=payload
    ).json()

    self.debug(r)

    return r

def delete(self, destinationId):
    endpoint = _uri_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      DESTINATION_ENDPOINT,
      _id=destinationId
    )

    r = requests.delete(
      endpoint,
      auth=self.getAuth()
    ).json()

    self.debug(r)

    return r


if __name__ == '__main__':
  d = Destination(
    debug=True
  )

  dd = d.getDetails('photograph_scalp')



    