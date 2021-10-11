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

    def create(self, service: str, groupId: str, trustCertificates: bool = False,
               runSetupTests: bool = True, config: dict, trustFingerprints: bool = False,
               ) -> dict:

        endpoint = _url_builder(
            self.getUrl()
        )

        payload = {
            "service": service,
            "group_id": groupId,
            "trust_certificates": trustCertificates,
            "run_setup_tests": runSetupTests,
            "config": config,
            "trust_fingerprints": trustFingerprints
        }

        r = self._post(
            endpoint,
            payload
        )

        self.debug(r)

        return r

    def modify(self, connectorId: str, paused: bool = False, syncFrequency: int = 30, trustCertificates: bool = False,
               runSetupTests bool=True, config: dict, auth: dict
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
        
    def delete(self, connectorId: str) -> str:

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