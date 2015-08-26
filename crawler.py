#-*-coding:utf-8-*-
import sys
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.crawler import Crawler
from scrapy import signals
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
reload(sys)
sys.setdefaultencoding('utf-8')

configure_logging
settings = get_project_settings()
runner = CrawlerRunner(settings)

@defer.inlineCallbacks

def crawl():
    #yield runner.crawl('userfollow')
    #yield runner.crawl('userinfo')
    yield runner.crawl('keyuser',keyword = sys.argv[1])
    yield runner.crawl('keyweibocontent',keyword = sys.argv[1])
    yield runner.crawl('userinfo',keyword = sys.argv[1]) 
    reactor.stop()

crawl()
#reactor.run()

#runner.crawl('keyweibocontent',keyword = sys.argv[1])
#runner.crawl('userinfo',keyword = sys.argv[1])
#d = runner.join()
#d.addBoth(lambda _:reactor.stop())
reactor.run()
#crawler = Crawler(settings)
#crawler.configure()
#crawler.crawl('keyuser',keyword = sys.argv[1])
#crawler.start()
