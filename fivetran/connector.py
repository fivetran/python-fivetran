import requests

from fivetran.fivetranapi import FivetranApi, _url_builder, BASE_ENDPOINT, CONNECTORS_ENDPOINT, CONNECTOR_METADATA_ENDPOINT

class InvalidResponseVersion(Exception): pass

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

    self._metadata_url = _url_builder(
      BASE_ENDPOINT,
      self.getVersion(),
      CONNECTOR_METADATA_ENDPOINT
    )

  def _set_response_headers(self, version):
    accepted_versions = [1, 2]

    if version == 1:
      return self.getHeaders()
    elif version == 2:
      return self.getV2Headers()
    else:
      raise InvalidRepsonseVersion(
        "Version must be one of {}".format(
          accepted_versions
        )
      )


  def getMetadataUrl(self):
    return self._metadata_url

  def getSourceMetadata(self, cursor: str = None, limit: int = 100) -> dict:
    param_dict = {
      "limit": limit,
      "cursor": cursor

    }
    query_params = _param_builder(param_dict)

    endpoint = _url_builder(
      self.getMetadataUrl(),
      _query_params=query_params
    )

    r = self._get(
      endpoint
    )

    self.debug(r)

    return r

  def getConfigMetadata(self, service: str) -> dict:
    endpoint = _url_builder(
      self.getMetadataUrl(),
      _path=service
    )

    r = self._get(
      endpoint
    )

    self.debug(r)

    return r

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

  def getDetails(self, connectorId: str, responseVersion: int = 2) -> dict:
    endpoint = _url_builder(
      self.getMetadataUrl(),
      _id=connectorId
    )

    r = self._get(
      endpoint,
      headers=self._set_response_headers()
    )

    self.debug(r)

    return r

  def modify(self, 
    connectorId: str, 
    config: dict = None,
    auth: dict = None,
    paused: bool = False,
    pauseAfterTrial: bool = False,
    trustCertificates: bool = False,
    trustFingerprints: bool = False,
    runSetupTests: bool = True,
    syncFrequency: int = 360, #6 hours
    dailySyncTime: str = None,
    scheduleType: str = 'auto',
    isHistoricalSync: bool = False
  ) -> dict:

    endpoint = _url_builder(
        self.getUrl(),
        _id=connectorId
    )

    payload = {
        "paused": paused,
        "pause_after_trial": pauseAfterTrial,
        "trust_certificates": trustCertificates,
        "trust_fingerprints": trustFingerprints,
        "run_setup_tests": runSetupTests,
        "sync_frequency": syncFrequency,
        "schedule_type": scheduleType,
        "is_historical_sync": isHistoricalSync
    }

    if config is not None:
      payload['config'] = config

    if auth is not None:
      payload['auth'] = auth

    if dailySyncTime is not None:
      payload['daily_sync_time'] = dailySyncTime

    r = self._patch(
      endpoint,
      payload
    )

    self.debug(r)

    return r

  def syncConnector(self, connectorId: str) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=connectorId,
      _path='force'
    )

    r = self._post(
      endpoint
    )
    
    self.debug(r)

    return r

  def resyncTable(self, connectorId: str, config: dict) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=connectorId,
      _path='schemas/tables/resync'
    )

    r = self._post(
      endpoint,
      config
    )

    self.debug(r)

    return r

  def runSetupTests(self, connectorId: str, trustCertificates: bool = False, trustFingerprints: bool = False) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=connectorId
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

  def deleteBulk(self, connectorIds:  list) -> dict:
    results = {}
    for connectorId in connectorIds:
      r = self.delete(
        connectorId
      )

      results[connectorId] = r

    return results

  def getSchemaConfig(self, connectorId: str) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=connectorId,
      _path='schemas'
    )

    r = self._get(
      endpoint
    )

    self.debug(r)

    return r

  def getTableConfig(self, connectorId: str, schemaName: str, tableName: str) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=connectorId,
      _path="schemas/{schemaName}/tables/{schemaName}/columns".format(
        schemaName=schemaName,
        tableName=tableName
      )
    )

    r = self._get(
      endpoint
    )

    self.debug(r)

    return r

  def reloadSchemaConfig(self, connectorId: str, excludeMode: str = 'PRESERVE') -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=connectorId,
      _path='schemas/reload'
    )

    payload = {
      "exclude_mode": excludeMode.upper()
    }

    r = self._post(
      endpoint,
      payload
    )

    self.debug(r)

    return r

  def modifySchemaConfig(self, connectorId: str, config: dict) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=connectorId,
      _path='schemas'
    )

    r = self._patch(
      endpoint,
      config
    )

    self.debug(r)

    return r

  def modifyDatabaseSchemaConfig(self, connectorId: str, schemaName: str, config: dict) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=connectorId,
      _path='schemas/{schemaName}'.format(
        schemaName=schemaName
      )
    )

    r = self._patch(
      endpoint,
      config
    )

  def modifyTableConfig(self, connectorId: str, schemaName: str, tableName: str, config: dict) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=connectorId,
      _path='schemas/{schemaName}/tables/{tableName}'.format(
        schemaName=schemaName,
        tableName=tableName
      )
    )

    r = self._patch(
      endpoint,
      config
    )

    self.debug(r)

    return r

  def modifyColumnConfig(self, connectorId: str, schemaName: str, tableName: str, columnName: str, config) -> dict:
    endpoint = _url_builder(
      self.getUrl(),
      _id=connectorId,
      _path='schemas/{schemaName}/tables/{tableName}/columns/{columnName}'.format(
        schemaName=schemaName,
        tableName=tableName,
        columnName=columnName
      )
    )

    r = self._patch(
      endpoint,
      config
    )

    self.debug(r)

    return r


if __name__ == '__main__':
  d = Connector(
      debug=True
  )

  dd = d.syncConnector('asdf  ')