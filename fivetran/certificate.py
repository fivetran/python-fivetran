from fivetran.fivetranapi import FivetranApi, _url_builder, BASE_ENDPOINT, CERTIFICATES_ENDPOINT, FINGERPRINTS_ENDPOINT, _param_builder
from fivetran.connector import Connector

class User(FivetranApi):
  def __init__(self, apiKey=None, apiSecret=None, version=None, debug=False):
    super().__init__(
      apiKey=apiKey, 
      apiSecret=apiSecret, 
      version=version, 
      debug=debug
    )

    self._certificates_url = _url_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      CERTIFICATES_ENDPOINT
    )

    self._fingerprints_url = _url_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      FINGERPRINTS_ENDPOINT

    )
    self._connector = Connector(
      apiKey=self.getApiKey(),
      apiSecret=self.getApiSecret(),
      version=self.getVersion(),
      debug=self.getDebug()
    )
  
  def getCertificatesUrl(self):
    return self._certificates_url

  def getFingerprintUrl(self):
    return self._fingerprints_url

  def approve(self, connectorId: str, hash: str, endcodedCert: str) -> dict:
    payload = {
      'connector_id': connectorId,
      'hash': hash,
      'encoded_cert': endcodedCert
    }

    r = self._post(
      self.getCertificatesUrl(),
      payload
    )

    self.debug(r)

    return r

  def getDetails(self, connectorId: str) -> list:
    r = self._connector.runSetupTests(
      connectorId=connectorId,
      trustCertificates=False
    )

    details = r['response']['data']['setup_tests']['details']

    return details

  def approveFingerprint(self, connectorId: str, hash: str, publicKey: str) -> dict:
    payload = {
      'connector_id': connectorId,
      'hash': hash,
      'public_key': publicKey
    }

    r = self._post(
      self.getFingerprintUrl(),
      payload
    )

    self.debug(r)

    return r


  def getFingerprintDetails(self, connectorId) -> list:
    r = self._connector.runSetupTests(
      connectorId=connectorId,
      trustCertificates=False
    )

    details = r['response']['data']['setup_tests']['details']

    return details









