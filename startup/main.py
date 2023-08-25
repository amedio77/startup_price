import schedule
import time
import os
import datetime


def run_scrapy_project():
    os.system("scrapy crawl startupprice")  # your_spider_name을 실제 스파이더 이름으로 변경


# 현재의 현지 시간을 얻습니다.
local_time = datetime.datetime.now()
print("server start!!")
print(local_time.strftime('%Y-%m-%d %H:%M:%S'))
# 매일 오전 9시에 스파이더를 실행
schedule.every().day.at("16:10").do(run_scrapy_project)

while True:
    schedule.run_pending()
    time.sleep(1)
