import os
import requests
import json

BASE_ENDPOINT = 'https://api.fivetran.com'
GROUPS_ENDPOINT = 'groups'
DESTINATIONS_ENDPOINT = 'destinations'
USERS_ENDPOINT = 'users'
CONNECTORS_ENDPOINT = 'connectors'
CONNECTOR_METADATA_ENDPOINT = 'metadata/connectors'
CERTIFICATES_ENDPOINT = 'certificates'

def _uri_builder(base_endpoint, version, api_endpoint, _id=None, _params=None):
  uri = "{}/{}/{}".format(
    base_endpoint,
    version,
    api_endpoint
  )

  if _id is not None:
    uri = "{}/{}".format(
      uri,
      _id
    )

  if _params is not None:
    uri = "{}/{}".format(
      uri,
      _params
    )

  return uri

class FivetranApi:
  def __init__(self, apiKey=None, apiSecret=None, version=None, debug=False):
    self._version = self._set_api_version(version)
    self._api_key = self._set_api_key(apiKey)
    self._api_secret = self._set_api_secret(apiKey)
    self._api_endpoint = None
    self._auth = requests.auth.HTTPBasicAuth(
      self._api_key,
      self._api_secret
    )
    self._debug = debug

  def _set_api_version(self, version):
    if version is None:
      version = 'v1'
    return version

  def _set_api_key(self, apiKey):
    if apiKey is None:
      apiKey = os.environ["FIVETRAN_APIKEY"]
    return apiKey

  def _set_api_secret(self, apiSecret):
    if apiSecret is None:
      apiSecret = os.environ['FIVETRAN_APISECRET']
    return apiSecret

  def _print(self, r):
    print(
      json.dumps(
        r,
        indent=4,
        sort_keys=True
      )
    )
    return r

  def debug(self, r):
    if self._debug:
      return self._print(r)

  def getAuth(self):
    return self._auth

  def getApiEndpoint(self):
    return self._api_endpoint

  def getVersion(self):
    return self._version