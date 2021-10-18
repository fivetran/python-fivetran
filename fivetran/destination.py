import requests

from fivetran.fivetranapi import FivetranApi, _url_builder, BASE_ENDPOINT, DESTINATIONS_ENDPOINT


class Destination(FivetranApi):
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
      DESTINATIONS_ENDPOINT
    )

  def create(
    self,
    groupId: str,
    service: str,
    timeZoneOffset: str,
    config: dict,
    region: str = 'US',
    trustCertificates: bool = False,
    trustFingerprints: bool = False,
    runSetupTests: bool = True
  ) -> dict:

    payload = {
      "group_id": groupId,
      "service": service,
      "time_zone_offset": timeZoneOffset,
      "config": config,
      "region": region,
      "trust_certificates": trustCertificates,
      "trust_fingerprints": trustFingerprints,
      "run_setup_tests": runSetupTests
    }

    r = self._post(
      endpoint,
      payload
    )

    self.debug(r)

    return r

  def getDetails(self, destinationId: str) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=destinationId
    )

    r = self._get(
      endpoint,
    )

    self.debug(r)

    return r

  def modify(
    self,
    destinationId: str,
    config: str = None,
    region: str = None,
    timeZoneOffset: str = None,
    trustCertificates: bool = False,
    trustFingerprints: bool = False,
    runSetupTests: bool = True
  ) -> dict:

    endpoint = _url_builder(
      self.getUrl(),
      _id=destinationId
    )

    payload = {
      "trust_certificates": trustCertificates,
      "trust_fingerprints": trustFingerprints,
      "run_setup_tests": runSetupTests
    }

    if region is not None:
      payload['region'] = region

    if timeZoneOffset is not None:
      payload['time_zone_offset'] = timeZoneOffset

    if config is not None:
      payload['config'] = config

    r = self._patch(
      endpoint,
      payload
    )

    self.debug(r)

    return r

  def runSetupTests(self, destinationId: str, trustCertificates: bool = False, trustFingerprints: bool = False) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=destinationId,
      _path='test'
    )

    payload = {
      "trust_certificates": trustCertificates,
      "trust_fingerprints": trustCertificates
    }

    r = self._post(
      endpoint,
      payload
    )

    self.debug(r)

    return r

  def delete(self, destinationId: str) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=destinationId
    )

    r = self._delete(
      endpoint
    )

    self.debug(r)

    return r

  def deleteBulk(self, destinationIds: list) -> dict:
    results = {}
    for destinationId in destinationIds:
      r = self._delete(
        destinationId
      )

      results[destinationId] = r

    return results

if __name__ == '__main__':
    d = Destination(
        debug=True
    )

    dd = d.getDetails('photograph_scalp')

    d.runSetupTests('photograph_scalp')
