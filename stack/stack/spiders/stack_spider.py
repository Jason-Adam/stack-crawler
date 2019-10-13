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
        questions = Selector(response).xpath('//div[@class="summary"]')

        for question in questions:
            item = StackItem()
            item["title"] = question.xpath(
                'h3/a[@class="question-hyperlink"]/text()'
            ).extract_first()
            item["url"] = question.xpath(
                'h3/a[@class="question-hyperlink"]/@href'
            ).extract_first()
            item["excerpt"] = question.xpath(
                'div[@class="excerpt"]/text()'
            ).extract_first()
            item["question"] = ""
            yield item
