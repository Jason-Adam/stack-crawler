from twisted.internet import reactor
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner
from stack.spiders.question_spider import QuestionSpider

configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
SETTINGS = get_project_settings()
RUNNER = CrawlerRunner(SETTINGS)

d = RUNNER.crawl(QuestionSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()
