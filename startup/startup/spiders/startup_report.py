from pathlib import Path

import scrapy
from ..database import DatabaseManager
from ..common import Util
from scrapy.exceptions import CloseSpider


class NewsSpider(scrapy.Spider):
    name = "report"

    def __init__(self, *args, **kwargs):
        super(NewsSpider, self).__init__(*args, **kwargs)
        self.db_manager = DatabaseManager()
        self.util = Util()

    def start_requests(self):
        base_url = "https://startuprecipe.co.kr/archives/invest-report/page/"
        last_date = self.db_manager.get_last_crawled_date()
        # 페이지 1부터 10까지 URL 생성
        for page_num in range(1, 5):
            url = base_url + str(page_num)
            self.log(f"Currently url: {url}")
            yield scrapy.Request(url=url, callback=self.parse, meta={'last_date': last_date} )

    def parse(self, response):
        # response.meta를 사용하여 last_date를 가져옵니다.
        last_date = response.meta['last_date']

        for article in response.css(
                '.vc_col-lg-12.vc_col-md-12.vc_col-sm-12.vc_col-xs-12.grid-item.masonry-block.blog-post-masonry'):
            item = {
                'title': article.css('h3 a span::text').get().strip(),
                'link': article.css('h3 a::attr(href)').get(),
                'date': article.css('.tags .tag:first-child::text').get().strip(),
                'category': 'report',
                'snippet': article.css('p::text').get().strip(),
            }
            comparison_result = self.util.compare_dates( last_date, item.get('date') );
            if comparison_result == 0 or comparison_result == 1:
                # 정상진행
                self.log(f"last_date_now : {last_date} / {item.get('date')} / {comparison_result}")
                # self.log(item)
                yield item

            elif comparison_result == -1:
                # 종료: 더 이상의 크롤링을 중단
                self.log(f"last_date_now : {last_date} / {item.get('date')} / {comparison_result}")
                self.log("이미 수집한 데이터 입니다.")
                raise CloseSpider("Your reason for closing the spider")  # 크롤링 종료
