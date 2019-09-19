import sys
from scrapy.cmdline import execute

if __name__ == '__main__':
    # execute(["scrapy","crawl","chouti","--nolog"])
    execute(["scrapy","crawlall","--nolog"])