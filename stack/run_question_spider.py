from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
from stack.spiders.stack_spider import StackSpider
from stack.spiders.question_spider import QuestionSpider

SETTINGS = get_project_settings()
RUNNER = CrawlerRunner(SETTINGS)


@defer.inlineCallbacks
def crawl():
    yield RUNNER.crawl(StackSpider)
    yield RUNNER.crawl(QuestionSpider)
    reactor.stop()


print("Starting Crawl")
crawl()
reactor.run()
print("Crawl Finished")
