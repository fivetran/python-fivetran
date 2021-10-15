from fivetran import connector
import copy

c = connector.Connector(
	debug=True
)
group_id = "proprietor_novelties"

imdb_base_config = {
    "service": "s3",
    "group_id": group_id,
    "schema": 'imdb',
    "role_arn": "arn:aws:iam::254359228911:role/ts-s3-demo-role",
    "bucket": "ts-s3-demo",
    "prefix": "imdb/",
    "file_type": "tsv",
    "compression": "uncompressed",
    "on_error": "skip",
    "append_file_option": "upsert_file",
    "null_sequence": "\\N",
    "delimiter": "\\t",
    "escape_char": '"',

}

imdb_filenames = [
  "name_basics.tsv",
  "title_akas.tsv",
  "title_basics.tsv",
  "title_crew.tsv",
  "title_episode.tsv",
  "title_principals.tsv",
  "title_ratings.tsv",
]

covid19_base_config = {
    "service": "s3",
    "group_id": group_id,
    "schema": 'covid_19',
    "role_arn": "arn:aws:iam::254359228911:role/ts-s3-demo-role",
    "bucket": "ts-s3-demo",
    "prefix": "covid_19/",
    "file_type": "csv",
    "compression": "uncompressed",
    "on_error": "skip",
    "append_file_option": "upsert_file",
    "delimiter": ","
}

covid19_filenames = [
  "anomalies.csv",         
  "prison_facilities.csv" , 
  "us_counties_2020.csv",    
  "us_rollup.csv",
  "colleges.csv",            
  "prison_systems.csv",      
  "us_counties_2021.csv",    
  "us_states.csv",
  "deaths.csv",              
  "us.csv",                  
  "us_counties_recent.csv",  
  "us_states_rollup.csv",
  "mask_use_by_county.csv",  
  "us_counties.csv",         
  "us_countries_rollup.csv"
]

animal_crossing_base_config = {
    "service": "s3",
    "group_id": group_id,
    "schema": 'animal_crossing',
    "role_arn": "arn:aws:iam::254359228911:role/ts-s3-demo-role",
    "bucket": "ts-s3-demo",
    "prefix": "animal_crossing/",
    "file_type": "csv",
    "compression": "uncompressed",
    "on_error": "skip",
    "append_file_option": "upsert_file",
    "delimiter": ","
}

animal_crossing_filenames = [
  "accessories.csv",
  "achievements.csv",
  "art.csv",
  "bags.csv",
  "bottoms.csv",
  "construction.csv",
  "dress_up.csv",
  "fencing.csv",
  "fish.csv",
  "floors.csv",
  "fossils.csv",
  "headwear.csv",
  "housewares.csv",
  "insects.csv",
  "miscellaneous.csv",
  "music.csv",
  "other.csv",
  "photos.csv",
  "posters.csv",
  "reactions.csv",
  "recipes.csv",
  "rugs.csv",
  "shoes.csv",
  "socks.csv",
  "tools.csv",
  "tops.csv",
  "umbrellas.csv",
  "villagers.csv",
  "wall_mounted.csv",
  "wallpaper.csv"
]

wine_base_config = {
    "service": "s3",
    "group_id": group_id,
    "schema": 'wine',
    "role_arn": "arn:aws:iam::254359228911:role/ts-s3-demo-role",
    "bucket": "ts-s3-demo",
    "prefix": "wine/",
    "file_type": "csv",
    "compression": "uncompressed",
    "on_error": "skip",
    "append_file_option": "upsert_file",
    "delimiter": ";"
}

wine_filenames = [
  "winequality_red.csv"
]

def createConfig(base_config, table, pattern):
    out = copy.deepcopy(base_config)

    out['table']  = table
    out['pattern'] = pattern

    return out

def bulkCreate(group_id, base_config, filenames):
  results = []

  for filename in filenames:
    config = createConfig(
      base_config,
      filename.split('.')[0],
      filename
    )

    result = c.create(
      groupId=group_id,
      service='s3',
      config=config,
      paused=False
    )

  return results

def loadCovid19Data():
  bulkCreate(
    group_id,
    covid19_base_config,
    covid19_filenames
  )

def loadAnimalCrossingData():
  bulkCreate(
    group_id,
    animal_crossing_base_config,
    animal_crossing_filenames
  )

def loadWineData():
  bulkCreate(
    group_id,
    wine_base_config,
    wine_filenames
  )

def loadImbdData():
  bulkCreate(
    group_id,
    imdb_base_config,
    imdb_filenames
  )


if __name__ == '__main__':
  loadAnimalCrossingData()
  loadWineData()
  # loadCovid19Data()
  # loadImbdData()

