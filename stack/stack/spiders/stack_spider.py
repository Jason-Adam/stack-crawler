from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "https://stackoverflow.com/questions/tagged/artificial-intelligence?tab=votes&page=1&pagesize=50",
        "https://stackoverflow.com/questions/tagged/artificial-intelligence?tab=votes&page=2&pagesize=50",
        "https://stackoverflow.com/questions/tagged/artificial-intelligence?tab=votes&page=3&pagesize=50",
        "https://stackoverflow.com/questions/tagged/artificial-intelligence?tab=votes&page=4&pagesize=50",
        "https://stackoverflow.com/questions/tagged/artificial-intelligence?tab=votes&page=5&pagesize=50",
        "https://stackoverflow.com/questions/tagged/artificial-intelligence?tab=votes&page=6&pagesize=50",
        "https://stackoverflow.com/questions/tagged/artificial-intelligence?tab=votes&page=7&pagesize=50",
        "https://stackoverflow.com/questions/tagged/artificial-intelligence?tab=votes&page=8&pagesize=50",
        "https://stackoverflow.com/questions/tagged/artificial-intelligence?tab=votes&page=9&pagesize=50",
        "https://stackoverflow.com/questions/tagged/artificial-intelligence?tab=votes&page=10&pagesize=50",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item["title"] = question.xpath(
                'a[@class="question-hyperlink"]/text()'
            ).extract()[0]
            item["url"] = question.xpath(
                'a[@class="question-hyperlink"]/@href'
            ).extract()[0]
            # item["question"] = question.xpath('div[@class="post-text"]/p').extract()
            yield item
