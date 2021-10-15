import requests

from fivetran.fivetranapi import FivetranApi, _url_builder, BASE_ENDPOINT, CONNECTORS_ENDPOINT, CONNECTOR_METADATA_ENDPOINT


class Connector(FivetranApi):
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
        CONNECTORS_ENDPOINT
    )

  def create(self, groupId: str, 
    service: str,
    config: dict,
    auth: dict = None,
    paused: bool = False,
    pauseAfterTrial: bool = False,
    trustCertificates: bool = False,
    trustFingerprints: bool = False,
    runSetupTests: bool = True,
    syncFrequency: int = 360, #6 hours
    dailySyncTime: str = None
  ) -> dict:

    endpoint = _url_builder(
        self.getUrl()
    )

    payload = {
      "group_id": groupId,
      "service": service,
      "config": config,
      "paused": paused,
      "pause_after_trial": pauseAfterTrial,
      "trust_certificates": trustCertificates,
      "trust_fingerprints": trustFingerprints,
      "run_setup_tests": runSetupTests,
      "sync_frequency": syncFrequency,
    }

    if auth is not None:
      payload['auth'] = auth

    if dailySyncTime is not None:
      payload['daily_sync_time'] = dailySyncTime

    r = self._post(
        endpoint,
        payload
    )

    self.debug(r)

    return r

  def modify(self, 
    connectorId: str, 
    config: dict, 
    auth: dict,
    paused: bool = False, 
    syncFrequency: int = 30, 
    trustCertificates: bool = False,
    runSetupTests: bool=True, 

  ) -> dict:

    endpoint = _url_builder(
        self.getUrl(),
        _id=connectorId
    )

    payload = {
        "paused": paused,
        "sync_frequency": syncFrequency,
        "trust_certificates": trustCertificates,
        "run_setup_tests": runSetupTests,
        "config": config,
        "auth": auth
    }

    r = self._patch(
      endpoint,
      payload
    )

    self.debug(r)

    return r
    
  def delete(self, connectorId: str) -> dict:

    endpoint = _url_builder(
      self.getUrl(),
      _id = connectorId
    )

    r = self._delete(
      endpoint
    )

    self.debug(r)

    return r

if __name__ == '__main__':
  d = Connector(
      debug=True
  )

  dd = d.create()