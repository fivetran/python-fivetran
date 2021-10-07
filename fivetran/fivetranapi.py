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

def _url_builder(base_endpoint, version=None, api_endpoint=None, _id=None, _path=None, _query_params=None):
  url = base_endpoint

  if version is not None:
    url = "{}/{}".format(
      url,
      version
    )

  if api_endpoint is not None:
    url = "{}/{}".format(
      url,
      api_endpoint
    )

  if _id is not None:
    url = "{}/{}".format(
      url,
      _id
    )

  if _path is not None:
    url = "{}/{}".format(
      url,
      _path
    )

  if _query_params is not None:
    url = "{}?{}".format(
      url,
      _query_params
    )

  return url

def _param_builder(param_dict):
  query_params = None

  for i, (key, value) in enumerate(param_dict.items()):
    if i == 0:
      if value is not None:
        query_params = '{}={}'.format(
          key,
          value
        )
      else:
        query_params = ''
    else:
      if value is not None:
        query_params = query_params + "&{}={}".format(
          key,
          value
        )

  if query_params is not None and query_params[0] == '&':
    query_params = query_params[1::]

  return query_params


class FivetranApi:
  def __init__(self, apiKey=None, apiSecret=None, version=None, debug=False):
    self._version = self._set_api_version(version)
    self._api_key = self._set_api_key(apiKey)
    self._api_secret = self._set_api_secret(apiKey)
    self._url = None
    self._auth = requests.auth.HTTPBasicAuth(
      self._api_key,
      self._api_secret
    )
    self._debug = debug

  def getUrl(self):
    return self._url

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
        sort_keys=True,
        default=str
      )
    )
    return r

  def _build_requests_output(self, statusCode, responseHeaders, response):
    output = {
      'status_code': statusCode,
      'headers': dict(responseHeaders), #avoids case insensitive dict error
      'response': response.json(),
      'raw_response': response

    }

    return output

  def _post(self, endpoint, payload=None):
    r = requests.post(
      endpoint,
      auth=self.getAuth(),
      json=payload
    )

    r = self._build_requests_output(
      r.status_code,
      r.headers,
      r
    )

    self.debug(r)

    return r

  def _get(self, endpoint):
    r = requests.get(
      endpoint,
      auth=self.getAuth()
    )

    r = self._build_requests_output(
      r.status_code,
      r.headers,
      r
    )

    self.debug(r)

    return r

  def _patch(self, endpoint, payload=None):
    r = requests.patch(
      endpoint,
      auth=self.getAuth(),
      json=payload
    )

    r = self._build_requests_output(
      r.status_code,
      r.headers,
      r
    )

    self.debug(r)

    return r

  def _put(self, endpoint, payload=None):
    r = requests.put(
      endpoint,
      auth=self.getAuth(),
      json=payload
    )

    r = self._build_requests_output(
      r.status_code,
      r.headers,
      r
    )


    self.debug(r)

    return r

  def _delete(self, endpoint, payload=None):
    r = requests.delete(
      endpoint,
      auth=self.getAuth()
    )

    r = self._build_requests_output(
      r.status_code,
      r.headers,
      r
    )

    self.debug(r)

    return r

  def _iterator(self, func, **kwargs):
    cursor = None
    limit = 100

    r = func(
      cursor=cursor,
      limit=limit,
      **kwargs
    )

    cursorExists = 'next_cursor' in r['response']['data'].keys()

    if cursorExists:
      cursor = r['response']['data']['next_cursor']

    while cursorExists:

      tmp = func(
        cursor=cursor,
        limit=limit,
        **kwargs
      )

      r['response']['data']['items'].extend(
        tmp['response']['data']['items']
      )

      cursorExists = 'next_cursor' in tmp['response']['data'].keys()
      if cursorExists:
        cursor = tmp['response']['data']['next_cursor']

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