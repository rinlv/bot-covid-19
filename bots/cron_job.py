import requests
import os
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

endpoint = os.environ['WEB_ENDPOINT']
interval = int(os.environ['INTERVAL'])

@sched.scheduled_job('interval', minutes=interval)
def timed_job():
    url = 'https://ncov.moh.gov.vn/dong-thoi-gian'
    response = requests.get(url, verify=False)
    page = BeautifulSoup(response.text.encode('utf-8'), "html.parser")
    source = 'Nguồn: ' + url
    latest_news = page.select('div.timeline-detail')[0]

    json = dict()
    json['last_update'] = latest_news.select('div.timeline-head')[0].get_text()
    json['news'] = latest_news.get_text() + '\n\n' + source 

    requests.post('{}/api/notify'.format(endpoint), json=json)

sched.start()