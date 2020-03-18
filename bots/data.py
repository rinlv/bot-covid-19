import requests
from bs4 import BeautifulSoup 
from bots.constants import *


def data(payload):
    response = requests.request("POST", URL, headers=HEADERS, data=payload)
    return response.json()

def formatMsg(confirmed, dead, recovered):
    return 'Nhiễm bệnh: ' + str(confirmed) + '\n\n Tử vong: ' + str(dead) + '\n\n Bình phục: ' + str(recovered)

def formatMsgProvince(confirmed, dead, recovered):
    return ' Nhiễm bệnh: ' + str(confirmed) + ' - Tử vong: ' + str(dead) + ' - Bình phục: ' + str(recovered)

def world():
    jsonStr = data(PAYLOAD_WORLD)
    title = 'Số ca nhiễm trên thế giới:'
    return title.upper() + '\n\n' + formatMsg(jsonStr[JSON_DATA_KEY][COLUMN_TOTAL_CONFIRMED], jsonStr[JSON_DATA_KEY][COLUMN_TOTAL_DEATHS], jsonStr[JSON_DATA_KEY][COLUMN_TOTAL_RECOVERED])

def default():
    jsonStr = data(PAYLOAD_PROVINCE)
    title = 'Số ca nhiễm ở Việt Nam: '
    message = ''
    total = 0
    for province in jsonStr[JSON_DATA_KEY][TABLE_PROVINCE]:
        total += int(province[COLUMN_CONFIRMED])
        message += '\n\n' + province[COLUMN_PROVINCE] + ':' + formatMsgProvince(province[COLUMN_CONFIRMED], province[COLUMN_DEATHS], province[COLUMN_RECOVERED])

    bigTitle = title + 'Tổng ' + str(total) + ' ca nhiễm trên ' + str(len(jsonStr[JSON_DATA_KEY][TABLE_PROVINCE])) + ' tỉnh thành'    
    return bigTitle.upper() + message

def news():
    url = 'https://ncov.moh.gov.vn/dong-thoi-gian'
    response = requests.get(url, verify=False)
    page = BeautifulSoup(response.text.encode('utf-8'), "html.parser")
    source = 'Nguồn: ' + url
    latest_news = page.select('div.timeline-detail')[0].get_text()
    return latest_news + '\n\n' + source 

def country(countryStr):
    jsonStr = data(PAYLOAD_COUNTRY)
    for country in jsonStr[JSON_DATA_KEY][TABLE_COUNTRY]:
        if (country[COLUMN_COUNTRY].lower() == countryStr.lower()):
            return 'Số ca nhiễm của ' + countryStr.upper() + ': \n\n' + formatMsg(country[COLUMN_CONFIRMED], country[COLUMN_DEATHS], country[COLUMN_RECOVERED])
    return default()

def list_country():
    jsonStr = data(PAYLOAD_COUNTRY)
    title = 'Danh sách các nước ghi nhận bệnh nhân nhiễm COVID-19: '
    message = ''
    for country in jsonStr[JSON_DATA_KEY][TABLE_COUNTRY]:
        message += '\n\n' + country[COLUMN_COUNTRY]

    return title + message