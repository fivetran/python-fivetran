from fivetran.fivetranapi import FivetranApi, _url_builder, BASE_ENDPOINT, CERTIFICATES_ENDPOINT, FINGERPRINTS_ENDPOINT, _param_builder

class Certificate(FivetranApi):
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
  
  def getCertificatesUrl(self):
    return self._certificates_url

  def getFingerprintUrl(self):
    return self._fingerprints_url

  def approveConnector(self, connectorId: str, hash: str, endcodedCert: str) -> dict:
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

  def approveConnectorFingerprint(self, connectorId: str, hash: str, publicKey: str) -> dict:
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

  def approveDestination(self, destinationId: str, hash: str, endcodedCert: str) -> dict:
    r = self.approveConnector(
      destinationId,
      hash,
      endcodedCert
    )

    return r


  def approveDestinationFingerprint(self, destinationId: str, hash: str, publicKey: str) -> dict:
    r = self.approveConnectorFingerprint(
      destinationId,
      hash,
      publicKey
    )

if __name__ == '__main__':
  certs = Certificate(debug=True)



