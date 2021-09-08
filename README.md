# Fivetran SDK for Python

`python-fivetran` is the official Fivetran SDK for the Python programming language.

Check out our (CHANGELOG)[https://github.com/fivetran-connorbrereton/python-fivetran/blob/master/CHANGELOG.md] for information about the latest bug fixes, updates, and features added to the SDK.

It is advised that you read the (documentation)[https://github.com/fivetran-connorbrereton/python-fivetran/blob/master/README.md] before using the SDK.

## Installation
```
git clone https://github.com/fivetran-connorbrereton/python-fivetran.git
```

## Getting Started
Initialize a new client by setting up your environment variables to be read.

```
$ touch .env
$ vi  .env

#inside the .env file...

API_KEY=yourkey
API_SECRET=yoursecret
```

## Examples
You can find examples of these API calls in an actual application (here)[https://github.com/fivetran-connorbrereton/Django-Code-Sample]

## API List

The following Fivetran REST API endpoints are implemented by the Fivetran SDK for the Python programming language. 

### [User Management API](https://fivetran.com/docs/rest-api/users)

REST API Endpoint | REST API Version | Development Status
--- | --- | ---
[List all Users](https://fivetran.com/docs/rest-api/users#listallusers) | v1 | Implemented
[Retrieve user details](https://fivetran.com/docs/rest-api/users#retrieveuserdetails) | v1 | Implemented
[Invite a user](https://fivetran.com/docs/rest-api/users#inviteauser) | v1 | Implemented
[Modify a user](https://fivetran.com/docs/rest-api/users#modifyauser) | v1 | Implemented
[Delete a user](https://fivetran.com/docs/rest-api/users#deleteauser) | v1 | Implemented

### [Group Management API](https://fivetran.com/docs/rest-api/groups)

REST API Endpoint | REST API Version | SDK Service
--- | --- | ---
[Create a group](https://fivetran.com/docs/rest-api/groups#createagroup) | v1 | Implemented
[List all groups](https://fivetran.com/docs/rest-api/groups#listallgroups) | v1 | Implemented
[Retrieve group details](https://fivetran.com/docs/rest-api/groups#retrievegroupdetails) | v1 | Implemented
[Modify a group](https://fivetran.com/docs/rest-api/groups#modifyagroup) | v1 | Implemented
[List all connectors within a group](https://fivetran.com/docs/rest-api/groups#listallconnectorswithinagroup) | v1 | Implemented
[List all users within a group](https://fivetran.com/docs/rest-api/groups#listalluserswithinagroup) | v1 | Implemented
[Add a user to a group](https://fivetran.com/docs/rest-api/groups#addausertoagroup) | v1 | Implemented
[Remove a user from a group](https://fivetran.com/docs/rest-api/groups#removeauserfromagroup) | v1 | Implemented
[Delete a group](https://fivetran.com/docs/rest-api/groups#deleteagroup) | v1 | Implemented

### [Destination Management API](https://fivetran.com/docs/rest-api/destinations)

REST API Endpoint | REST API Version | SDK Service/Config
--- | --- | ---
[Create a destination](https://fivetran.com/docs/rest-api/destinations#createadestination) | v1 | Implemented
[Retrieve destination details](https://fivetran.com/docs/rest-api/destinations#retrievedestinationdetails) | v1 | Implemented
[Modify a destination](https://fivetran.com/docs/rest-api/destinations#modifyadestination) | v1 | Implemented
[Run destination setup tests](https://fivetran.com/docs/rest-api/destinations#rundestinationsetuptests) | v1 | Implemented
[Delete a destination](https://fivetran.com/docs/rest-api/destinations#deleteadestination) | v1 | Implemented
[Destination Config](https://fivetran.com/docs/rest-api/destinations/config) | v1 | Implemented

### [Connector Management API](https://fivetran.com/docs/rest-api/connectors)

REST API Endpoint | REST API Version | SDK Service/Config/Auth
--- | --- | ---
[Retrieve source metadata](https://fivetran.com/docs/rest-api/connectors#retrievesourcemetadata) | v1 | Implemented
[Create a connector](https://fivetran.com/docs/rest-api/connectors#createaconnector) | v2 | Implemented
[Retrieve connector details](https://fivetran.com/docs/rest-api/connectors#retrieveconnectordetails) | v2 | Implemented
[Modify a connector](https://fivetran.com/docs/rest-api/connectors#modifyaconnector) | v2 | Implemented
[Sync connector data](https://fivetran.com/docs/rest-api/connectors#syncconnectordata) | v1 | Implemented
[Re-sync connector table data](https://fivetran.com/docs/rest-api/connectors#resyncconnectortabledata) | v1 | Implemented
[Run connector setup tests](https://fivetran.com/docs/rest-api/connectors#runconnectorsetuptests) | v2 | Implemented
[Delete a connector](https://fivetran.com/docs/rest-api/connectors#deleteaconnector) | v1 | Implemented
[Retrieve a connector schema config](https://fivetran.com/docs/rest-api/connectors#retrieveaconnectorschemaconfig) | v1 | Implemented
[Retrieve source table columns config](https://fivetran.com/docs/rest-api/connectors#retrievesourcetablecolumnsconfig) | v1 | Implemented
[Reload a connector schema config](https://fivetran.com/docs/rest-api/connectors#reloadaconnectorschemaconfig) | v1 | Implemented
[Modify a connector schema config](https://fivetran.com/docs/rest-api/connectors#modifyaconnectorschemaconfig) | v1 | Implemented
[Modify a connector database schema config](https://fivetran.com/docs/rest-api/connectors#modifyaconnectordatabaseschemaconfig) | v1 | Implemented
[Modify a connector table config](https://fivetran.com/docs/rest-api/connectors#modifyaconnectortableconfig) | v1 | Implemented
[Modify a connector column config](https://fivetran.com/docs/rest-api/connectors#modifyaconnectorcolumnconfig) | v1 | Implemented
[Connector Config](https://fivetran.com/docs/rest-api/connectors/config) | v1 | Implemented
[Connector Auth](https://fivetran.com/docs/rest-api/connectors) | v1 | Implemented
[Connect Card](https://fivetran.com/docs/rest-api/connectors/connect-card) | v1 | Implemented

### [Certificate Management API](https://fivetran.com/docs/rest-api/certificates)
REST API Endpoint | REST API Version | SDK Service
--- | --- | ---
[Approve a connector certificate](https://fivetran.com/docs/rest-api/certificates#approveaconnectorcertificate) | v1 | Implemented
[Approve a connector fingerprint](https://fivetran.com/docs/rest-api/certificates#approveaconnectorfingerprint) | v1 | Implemented
[Approve a destination certificate](https://fivetran.com/docs/rest-api/certificates#approveadestinationcertificate) | v1 | Implemented
[Approve a destination fingerprint](https://fivetran.com/docs/rest-api/certificates#approveadestinationfingerprint) | v1 | Implemented
## Support

Please get in touch with us through our [Support Portal](https://support.fivetran.com/) if you 
have any comments, suggestions, support requests, or bug reports.  