import os
from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem

SO_TAG = os.environ.get("SO_TAG")


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        f"https://stackoverflow.com/questions/tagged/{SO_TAG}?tab=Votes&page=1&pagesize=50",
        f"https://stackoverflow.com/questions/tagged/{SO_TAG}?tab=Votes&page=2&pagesize=50",
        f"https://stackoverflow.com/questions/tagged/{SO_TAG}?tab=Votes&page=3&pagesize=50",
        f"https://stackoverflow.com/questions/tagged/{SO_TAG}?tab=Votes&page=4&pagesize=50",
        f"https://stackoverflow.com/questions/tagged/{SO_TAG}?tab=Votes&page=5&pagesize=50",
        f"https://stackoverflow.com/questions/tagged/{SO_TAG}?tab=Votes&page=6&pagesize=50",
        f"https://stackoverflow.com/questions/tagged/{SO_TAG}?tab=Votes&page=7&pagesize=50",
        f"https://stackoverflow.com/questions/tagged/{SO_TAG}?tab=Votes&page=8&pagesize=50",
        f"https://stackoverflow.com/questions/tagged/{SO_TAG}?tab=Votes&page=9&pagesize=50",
        f"https://stackoverflow.com/questions/tagged/{SO_TAG}?tab=Votes&page=10&pagesize=50",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]')

        for question in questions:
            item = StackItem()
            item["url"] = question.xpath(
                'h3/a[@class="question-hyperlink"]/@href'
            ).extract_first()
            item["title"] = question.xpath(
                'h3/a[@class="question-hyperlink"]/text()'
            ).extract_first()
            item["question"] = ""
            yield item
