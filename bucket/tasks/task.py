from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from ..models import Download

import urllib.request
import os

def download():
    print("download")
    data_links = Download.objects.filter(finish=False)
    for link in data_links:
        filename = link.url.split('/')[-1]
        data = urllib.request.urlopen(link.url).read()
        putPath = "bucket/downloads/"+link.user.username+"/"
        os.makedirs(putPath,exist_ok=True)
        with open(putPath+filename,mode="wb+") as f:
            f.write(data)
            link.finish = True
    print("end")

def start():
    scheduler = BackgroundScheduler()
    print("schedule start")
    scheduler.add_job(download,'cron',hour=9,minute=33)
    scheduler.start()
