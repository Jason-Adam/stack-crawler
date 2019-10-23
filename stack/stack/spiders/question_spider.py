import os
import re
from urllib.parse import urljoin
from pymongo import MongoClient, collection
from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem

MONGO_DB = os.environ.get("MONGO_DB")
MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION")
MONGO_HOST = os.environ.get("MONGO_HOST")
MONGO_PORT = int(os.environ.get("MONGO_PORT"))


tag = re.compile("<.+?>")


def get_question_paths():
    client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
    db = client[MONGO_DB]
    ai = collection.Collection(database=db, name=MONGO_COLLECTION)
    cursor = ai.find({})
    urls = [i["url"] for i in cursor]
    return [urljoin("https://stackoverflow.com", url) for url in urls]


class QuestionSpider(Spider):
    name = "question"
    allowed_domains = ["stackoverflow.com"]
    start_urls = get_question_paths()

    def parse(self, response):
        question = Selector(response).xpath('//div[@id="content"]')
        item = StackItem()
        item["url"] = question.xpath(
            '//div[@id="question-header"]/h1/a[@class="question-hyperlink"]/@href'
        ).extract_first()
        q_text = response.xpath(
            '//div[@class="postcell post-layout--right"]/div[@class="post-text"]/p'
        )
        q_text = [i.extract() for i in q_text]
        q_text = " ".join(q_text)
        q_text = tag.sub("", q_text)
        item["question"] = q_text
        yield item
