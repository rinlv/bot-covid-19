URL = 'https://corona-api.kompa.ai/graphql'

COLUMN_COUNTRY = 'Country_Region'
COLUMN_PROVINCE = 'Province_Name'
COLUMN_CONFIRMED = 'Confirmed'
COLUMN_DEATHS = 'Deaths'
COLUMN_RECOVERED = 'Recovered'
COLUMN_LAST_UPDATE = 'Last_Update'
COLUMN_TOTAL_CONFIRMED = 'totalConfirmed'
COLUMN_TOTAL_DEATHS = 'totalDeaths'
COLUMN_TOTAL_RECOVERED = 'totalRecovered'

TABLE_COUNTRY = 'countries'
TABLE_PROVINCE = 'provinces'

JSON_DATA_KEY = 'data'

HEADERS = {
  'authority': 'corona-api.kompa.ai',
  'method': 'POST',
  'path': '/graphql',
  'scheme': 'https',
  'accept': '*/*',
  'Content-Type': 'application/json',
  'sec-fetch-dest': '',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'origin': 'https://corona.kompa.ai',
  'referer': 'https://corona.kompa.ai/'
}

PAYLOAD_WORLD = '{\n    "query": "query countries { totalDeaths totalConfirmed totalRecovered }"\n}'
PAYLOAD_PROVINCE = '{\n  "query": "query provinces {  provinces {    Province_Name   Confirmed    Deaths    Recovered    Last_Update  }}"\n}'
PAYLOAD_COUNTRY = '{\n  "query": "query countries { countries {   Country_Region    Confirmed   Deaths    Recovered Last_Update }}"\n}'

COMMAND_WORLD = "world"
COMMAND_NEWS = "news"
COMMAND_COUNTRY = "all"