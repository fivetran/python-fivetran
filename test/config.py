from fivetran import destination

d = destination.Destination(
  debug=True
)

def createDestination(group_id, service, time_zone_offset, config)
  results = d.create(
    groupId=group_id,
    service=service,
    timeZoneOffset=time_zone_offset,
    config=config,
    trustCertificates=True,
    trustFingerprints=True,
    runSetupTests=True
  )

  return results

#postgres, mysql, sql_server (all flavors)
#database is iqnored for mysql

group_id = 'proprietor_novelties'
service = ''
time_zone_offset = '-7'
database_config = {
  "host": "",
  "port": 5432,
  "database": "",
  "user": "fivetranadmin",
  "password": ""
}


if __name__ == '__main__':
  createDestination(
    group_id,
    service,
    time_zone_offset,
    database_config
  )