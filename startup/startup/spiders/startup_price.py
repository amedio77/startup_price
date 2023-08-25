from pathlib import Path

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "startupprice"

    def start_requests(self):
        base_url = "https://startuprecipe.co.kr/page/"
        # 페이지 1부터 10까지 URL 생성
        for page_num in range(1, 3):
            url = base_url + str(page_num)
            self.log(f"Currently url: {url}")
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for article in response.css('.blog-post-masonry'):
            item = {
                'date': article.css('.tags .tag:first-child::text').get().strip(),
                'category': article.css('.tags .tag:last-child::text').get().strip(),
                'title': article.css('h3 a span::text').get().strip(),
                'link': article.css('h3 a::attr(href)').get(),
                'snippet': article.css('p::text').get().strip(),
            }

            # 추출된 값을 출력합니다.
            self.log(item)
            yield item
