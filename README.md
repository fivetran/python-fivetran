# Fivetran SDK for Python

`python-fivetran` is the official Fivetran SDK for the Python programming language.

Check out our (CHANGELOG)[] for information about the latest bug fixes, updates, and features added to the SDK.

It is advised that you read the (documentation)[] before using the SDK.

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

REST API Endpoint | REST API Version | SDK Service
--- | --- | ---
[List all Users](https://fivetran.com/docs/rest-api/users#listallusers) | v1 | [UsersListService](https://pkg.go.dev/github.com/fivetran/go-fivetran#UsersListService)
[Retrieve user details](https://fivetran.com/docs/rest-api/users#retrieveuserdetails) | v1 | [UserDetailsService](https://pkg.go.dev/github.com/fivetran/go-fivetran#UserDetailsService)
[Invite a user](https://fivetran.com/docs/rest-api/users#inviteauser) | v1 | [UserInviteService](https://pkg.go.dev/github.com/fivetran/go-fivetran#UserInviteService) 
[Modify a user](https://fivetran.com/docs/rest-api/users#modifyauser) | v1 | [UserModifyService](https://pkg.go.dev/github.com/fivetran/go-fivetran#UserModifyService)
[Delete a user](https://fivetran.com/docs/rest-api/users#deleteauser) | v1 | [UserDeleteService](https://pkg.go.dev/github.com/fivetran/go-fivetran#UserDeleteService)

### [Group Management API](https://fivetran.com/docs/rest-api/groups)

REST API Endpoint | REST API Version | SDK Service
--- | --- | ---
[Create a group](https://fivetran.com/docs/rest-api/groups#createagroup) | v1 | [GroupCreateService](https://pkg.go.dev/github.com/fivetran/go-fivetran#GroupCreateService)
[List all groups](https://fivetran.com/docs/rest-api/groups#listallgroups) | v1 | [GroupsListService](https://pkg.go.dev/github.com/fivetran/go-fivetran#GroupsListService)
[Retrieve group details](https://fivetran.com/docs/rest-api/groups#retrievegroupdetails) | v1 | [GroupDetailsService](https://pkg.go.dev/github.com/fivetran/go-fivetran#GroupDetailsService)
[Modify a group](https://fivetran.com/docs/rest-api/groups#modifyagroup) | v1 | [GroupModifyService](https://pkg.go.dev/github.com/fivetran/go-fivetran#GroupModifyService)
[List all connectors within a group](https://fivetran.com/docs/rest-api/groups#listallconnectorswithinagroup) | v1 | [GroupListConnectorsService](https://pkg.go.dev/github.com/fivetran/go-fivetran#GroupListConnectorsService)
[List all users within a group](https://fivetran.com/docs/rest-api/groups#listalluserswithinagroup) | v1 | [GroupListUsersService](https://pkg.go.dev/github.com/fivetran/go-fivetran#GroupListUsersService)
[Add a user to a group](https://fivetran.com/docs/rest-api/groups#addausertoagroup) | v1 | [GroupAddUserService](https://pkg.go.dev/github.com/fivetran/go-fivetran#GroupAddUserService)
[Remove a user from a group](https://fivetran.com/docs/rest-api/groups#removeauserfromagroup) | v1 | [GroupRemoveUserService](https://pkg.go.dev/github.com/fivetran/go-fivetran#GroupRemoveUserService)
[Delete a group](https://fivetran.com/docs/rest-api/groups#deleteagroup) | v1 | [GroupDeleteService](https://pkg.go.dev/github.com/fivetran/go-fivetran#GroupDeleteService)

### [Destination Management API](https://fivetran.com/docs/rest-api/destinations)

REST API Endpoint | REST API Version | SDK Service/Config
--- | --- | ---
[Create a destination](https://fivetran.com/docs/rest-api/destinations#createadestination) | v1 | [DestinationCreateService](https://pkg.go.dev/github.com/fivetran/go-fivetran#DestinationCreateService)
[Retrieve destination details](https://fivetran.com/docs/rest-api/destinations#retrievedestinationdetails) | v1 | [DestinationDetailsService](https://pkg.go.dev/github.com/fivetran/go-fivetran#DestinationDetailsService)
[Modify a destination](https://fivetran.com/docs/rest-api/destinations#modifyadestination) | v1 | [DestinationModifyService](https://pkg.go.dev/github.com/fivetran/go-fivetran#DestinationModifyService)
[Run destination setup tests](https://fivetran.com/docs/rest-api/destinations#rundestinationsetuptests) | v1 | [DestinationSetupTestsService](https://pkg.go.dev/github.com/fivetran/go-fivetran#DestinationSetupTestsService)
[Delete a destination](https://fivetran.com/docs/rest-api/destinations#deleteadestination) | v1 | [DestinationDeleteService](https://pkg.go.dev/github.com/fivetran/go-fivetran#DestinationDeleteService)
[Destination Config](https://fivetran.com/docs/rest-api/destinations/config) | v1 | [DestinationConfig](https://pkg.go.dev/github.com/fivetran/go-fivetran#DestinationConfig)

### [Connector Management API](https://fivetran.com/docs/rest-api/connectors)

REST API Endpoint | REST API Version | SDK Service/Config/Auth
--- | --- | ---
[Retrieve source metadata](https://fivetran.com/docs/rest-api/connectors#retrievesourcemetadata) | v1 | [ConnectorsSourceMetadataService](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorsSourceMetadataService)
[Create a connector](https://fivetran.com/docs/rest-api/connectors#createaconnector) | v2 | [ConnectorCreateService](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorCreateService)
[Retrieve connector details](https://fivetran.com/docs/rest-api/connectors#retrieveconnectordetails) | v2 | [ConnectorDetailsService](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorDetailsService)
[Modify a connector](https://fivetran.com/docs/rest-api/connectors#modifyaconnector) | v2 | [ConnectorModifyService](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorModifyService)
[Sync connector data](https://fivetran.com/docs/rest-api/connectors#syncconnectordata) | v1 | [ConnectorSyncService](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorSyncService)
[Re-sync connector table data](https://fivetran.com/docs/rest-api/connectors#resyncconnectortabledata) | v1 | [ConnectorReSyncTableService](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorReSyncTableService)
[Run connector setup tests](https://fivetran.com/docs/rest-api/connectors#runconnectorsetuptests) | v2 | [ConnectorSetupTestsService](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorSetupTestsService)
[Delete a connector](https://fivetran.com/docs/rest-api/connectors#deleteaconnector) | v1 | [ConnectorDeleteService](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorDeleteService)
[Retrieve a connector schema config](https://fivetran.com/docs/rest-api/connectors#retrieveaconnectorschemaconfig) | | not implemented
[Retrieve source table columns config](https://fivetran.com/docs/rest-api/connectors#retrievesourcetablecolumnsconfig) | | not implemented
[Reload a connector schema config](https://fivetran.com/docs/rest-api/connectors#reloadaconnectorschemaconfig) | | not implemented
[Modify a connector schema config](https://fivetran.com/docs/rest-api/connectors#modifyaconnectorschemaconfig) | | not implemented
[Modify a connector database schema config](https://fivetran.com/docs/rest-api/connectors#modifyaconnectordatabaseschemaconfig) | | not implemented
[Modify a connector table config](https://fivetran.com/docs/rest-api/connectors#modifyaconnectortableconfig) | | not implemented
[Modify a connector column config](https://fivetran.com/docs/rest-api/connectors#modifyaconnectorcolumnconfig) | | not implemented
[Connector Config](https://fivetran.com/docs/rest-api/connectors/config) | v1 | [ConnectorConfig](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorConfig)<br> [ConnectorConfigReports](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorConfigReports)<br> [ConnectorConfigProjectCredentials](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorConfigProjectCredentials)<br> [ConnectorConfigCustomTables](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorConfigCustomTables)
[Connector Auth](https://fivetran.com/docs/rest-api/connectors) | v1 | [ConnectorAuth](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorAuth)<br> [ConnectorAuthClientAccess](https://pkg.go.dev/github.com/fivetran/go-fivetran#ConnectorAuthClientAccess)
[Connect Card](https://fivetran.com/docs/rest-api/connectors/connect-card) | | not implemented

### [Certificate Management API](https://fivetran.com/docs/rest-api/certificates)
REST API Endpoint | REST API Version | SDK Service
--- | --- | ---
[Approve a connector certificate](https://fivetran.com/docs/rest-api/certificates#approveaconnectorcertificate) | v1 | [CertificateConnectorCertificateApproveService](https://pkg.go.dev/github.com/fivetran/go-fivetran#CertificateConnectorCertificateApproveService)
[Approve a connector fingerprint](https://fivetran.com/docs/rest-api/certificates#approveaconnectorfingerprint) | v1 | [CertificateConnectorFingerprintApproveService](https://pkg.go.dev/github.com/fivetran/go-fivetran#CertificateConnectorFingerprintApproveService)
[Approve a destination certificate](https://fivetran.com/docs/rest-api/certificates#approveadestinationcertificate) | v1 | [CertificateDestinationCertificateApproveService](https://pkg.go.dev/github.com/fivetran/go-fivetran#CertificateDestinationCertificateApproveService)
[Approve a destination fingerprint](https://fivetran.com/docs/rest-api/certificates#approveadestinationfingerprint) | v1 | [CertificateDestinationFingerprintApproveService](https://pkg.go.dev/github.com/fivetran/go-fivetran#CertificateDestinationFingerprintApproveService)

## Support

Please get in touch with us through our [Support Portal](https://support.fivetran.com/) if you 
have any comments, suggestions, support requests, or bug reports.  