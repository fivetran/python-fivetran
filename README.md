# Fivetran SDK for Python

`python-fivetran` is the official Fivetran SDK for the Python programming language.

Check out our [CHANGELOG](https://github.com/fivetran-connorbrereton/python-fivetran/blob/master/CHANGELOG.md) for information about the latest bug fixes, updates, and features added to the SDK.

It is advised that you read the [documentation](https://github.com/fivetran-connorbrereton/python-fivetran/blob/master/README.md) before using the SDK.

## Installation
* Clone the Sales Engineers repo via: `git clone https://github.com/fivetran/sales-engineers.git`
* Navigate to `python-fivetran`
* Run `pip3 install -e .`
* You now have the SDK installed as a local Python package

## Getting Started
Add the Fivetran API Key and API Secret to your environment variables. 

Note that variables can also be passed into a class upon instantiation, but for more secure code the environment variable approach is recommended.
* Open your terminal and run `nano ~/.bash_profile` 
* Add the following
```
export FIVETRAN_APIKEY="your api key"
export FIVETRAN_APISECRET="your api secret"
```
* Save and Exit
* With your CLI type in `source ~/.bash_profile`
* To have this done automatically whenever you open up your terminal do the following
  * Open your terminal and run `nano ~/.bashrc`
  * Add the following: `source ~/.bash_profile`
  * Save and Exit

## Usage
There are 5 main files that contain the Python implementation of all the possible REST API calls:
1. connectors.py
2. destinations.py
3. groups.py
4. users.py
5. certificates.py

Each file contains the corresponding Class that houses all the methods specfic to that REST API endpoint. The `fivetranapi.py` file contains all the base methods that all other classes inherit. It is not necessary to interface with this file.

* To use the API create a new file (e.g., `sdk_demo.py`)
* Import the necessary modules for your code:
```python
from fivetran import connector
from fivetran import group
#so on and so forth
```
* To instaniate a class do the following:
```python
from fivetran import group

g = group.Group(
	debug=True
)
```
* To use a method in the class simply call that method. Names are analogous to the REST API
```python
from fivetran import group

g = group.Group(
	debug=True
)

groupDetails = g.getDetails(
	groupId='photograph_scalp'
)

#so on an so forth
```

* An overview of all methods and classes can be found in `python-fivetran/docs`. They're in HTML format and render nicely in a browser.


## API List

The following Fivetran REST API endpoints are implemented by the Fivetran SDK for the Python programming language. 

### [User Management API](https://fivetran.com/docs/rest-api/users)

REST API Endpoint | REST API Version |
--- | --- |
[List all Users](https://fivetran.com/docs/rest-api/users#listallusers) | v1 |
[Retrieve user details](https://fivetran.com/docs/rest-api/users#retrieveuserdetails) | v1 |
[Invite a user](https://fivetran.com/docs/rest-api/users#inviteauser) | v1 |
[Modify a user](https://fivetran.com/docs/rest-api/users#modifyauser) | v1 |
[Delete a user](https://fivetran.com/docs/rest-api/users#deleteauser) | v1 |

### [Group Management API](https://fivetran.com/docs/rest-api/groups)

REST API Endpoint | REST API Version |
--- | --- |
[Create a group](https://fivetran.com/docs/rest-api/groups#createagroup) | v1 |
[List all groups](https://fivetran.com/docs/rest-api/groups#listallgroups) | v1 |
[Retrieve group details](https://fivetran.com/docs/rest-api/groups#retrievegroupdetails) | v1 |
[Modify a group](https://fivetran.com/docs/rest-api/groups#modifyagroup) | v1 |
[List all connectors within a group](https://fivetran.com/docs/rest-api/groups#listallconnectorswithinagroup) | v1 |
[List all users within a group](https://fivetran.com/docs/rest-api/groups#listalluserswithinagroup) | v1 |
[Add a user to a group](https://fivetran.com/docs/rest-api/groups#addausertoagroup) | v1 |
[Remove a user from a group](https://fivetran.com/docs/rest-api/groups#removeauserfromagroup) | v1 |
[Delete a group](https://fivetran.com/docs/rest-api/groups#deleteagroup) | v1 |

### [Destination Management API](https://fivetran.com/docs/rest-api/destinations)

REST API Endpoint | REST API Version |
--- | --- |
[Create a destination](https://fivetran.com/docs/rest-api/destinations#createadestination) | v1 |
[Retrieve destination details](https://fivetran.com/docs/rest-api/destinations#retrievedestinationdetails) | v1 |
[Modify a destination](https://fivetran.com/docs/rest-api/destinations#modifyadestination) | v1 |
[Run destination setup tests](https://fivetran.com/docs/rest-api/destinations#rundestinationsetuptests) | v1 |
[Delete a destination](https://fivetran.com/docs/rest-api/destinations#deleteadestination) | v1 |
[Destination Config](https://fivetran.com/docs/rest-api/destinations/config) | v1 |

### [Connector Management API](https://fivetran.com/docs/rest-api/connectors)

REST API Endpoint | REST API Version |
--- | --- |
[Retrieve source metadata](https://fivetran.com/docs/rest-api/connectors#retrievesourcemetadata) | v1 |
[Create a connector](https://fivetran.com/docs/rest-api/connectors#createaconnector) | v2 |
[Retrieve connector details](https://fivetran.com/docs/rest-api/connectors#retrieveconnectordetails) | v2 |
[Modify a connector](https://fivetran.com/docs/rest-api/connectors#modifyaconnector) | v2 |
[Sync connector data](https://fivetran.com/docs/rest-api/connectors#syncconnectordata) | v1 |
[Re-sync connector table data](https://fivetran.com/docs/rest-api/connectors#resyncconnectortabledata) | v1 |
[Run connector setup tests](https://fivetran.com/docs/rest-api/connectors#runconnectorsetuptests) | v2 |
[Delete a connector](https://fivetran.com/docs/rest-api/connectors#deleteaconnector) | v1 |
[Retrieve a connector schema config](https://fivetran.com/docs/rest-api/connectors#retrieveaconnectorschemaconfig) | v1 |
[Retrieve source table columns config](https://fivetran.com/docs/rest-api/connectors#retrievesourcetablecolumnsconfig) | v1 |
[Reload a connector schema config](https://fivetran.com/docs/rest-api/connectors#reloadaconnectorschemaconfig) | v1 |
[Modify a connector schema config](https://fivetran.com/docs/rest-api/connectors#modifyaconnectorschemaconfig) | v1 |
[Modify a connector database schema config](https://fivetran.com/docs/rest-api/connectors#modifyaconnectordatabaseschemaconfig) | v1 |
[Modify a connector table config](https://fivetran.com/docs/rest-api/connectors#modifyaconnectortableconfig) | v1 |
[Modify a connector column config](https://fivetran.com/docs/rest-api/connectors#modifyaconnectorcolumnconfig) | v1 |
[Connector Config](https://fivetran.com/docs/rest-api/connectors/config) | v1 |
[Connector Auth](https://fivetran.com/docs/rest-api/connectors) | v1 |
[Connect Card](https://fivetran.com/docs/rest-api/connectors/connect-card) | v1 |

### [Certificate Management API](https://fivetran.com/docs/rest-api/certificates)
REST API Endpoint | REST API Version |
--- | --- |
[Approve a connector certificate](https://fivetran.com/docs/rest-api/certificates#approveaconnectorcertificate) | v1 |
[Approve a connector fingerprint](https://fivetran.com/docs/rest-api/certificates#approveaconnectorfingerprint) | v1 |
[Approve a destination certificate](https://fivetran.com/docs/rest-api/certificates#approveadestinationcertificate) | v1 |
[Approve a destination fingerprint](https://fivetran.com/docs/rest-api/certificates#approveadestinationfingerprint) | v1 |
