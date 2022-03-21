# Fivetran SDK for Python

Check out our [CHANGELOG](https://github.com/fivetran-connorbrereton/python-fivetran/blob/master/CHANGELOG.md) for information about the latest bug fixes, updates, and features added to the code snippets.

It is advised that you read the [documentation](https://github.com/fivetran-connorbrereton/python-fivetran/blob/master/README.md) alongside the code snippets.

## Installation
```
git clone https://github.com/fivetran-connorbrereton/python-fivetran.git
```

## Getting Started
Initialize a new client by setting up your environment variables to be read.

```
$ touch .env
$ vi  .env

# set the environment variables API_KEY and API_SECRET in the method of your choice.

API_KEY=yourkey
API_SECRET=yoursecret
```

## Examples
You can find examples of these API calls in an actual application [here](https://github.com/fivetran-connorbrereton/Django-Code-Sample)

## API List

The following Fivetran REST API endpoints are implemented as code snippets in this repository. 

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
## Support

Please get in touch with us through our [Support Portal](https://support.fivetran.com/) if you 
have any comments, suggestions, support requests, or bug reports.
