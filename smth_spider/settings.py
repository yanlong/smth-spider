# -*- coding: utf-8 -*-

# Scrapy settings for smth_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'smth_spider'

SPIDER_MODULES = ['smth_spider.spiders']
NEWSPIDER_MODULE = 'smth_spider.spiders'

#MONGO_URI='mongodb://127.0.0.1:27017'
MONGO_URI='mongodb://127.0.0.1:8100'
MONGO_DATABASE='smth'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'smth_spider (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
'Cookie': '_ga=GA1.2.316291097.1429852824; Hm_lvt_7734e0ab76401586c0e18dc2feefc01b=1441631966; bfd_g=9de2782bcb754fd70000689300906e3054c9fda8; tma=88525828.7971704.1429693672137.1449543590241.1449629553140.142; tmd=2533.88525828.7971704.1429693672137.; main[UTMPUSERID]=gomypig; main[UTMPKEY]=28696048; main[UTMPNUM]=12483; main[PASSWORD]=%2503d%2500a2%2540%2526%250D%2516%250923%251Bu%2509%252C%250D%2522%2507Vg%2523%2504%250E; main[XWJOKE]=hoho; Hm_lvt_9c7f4d9b7c00cb5aba2c637c64a41567=1457776174,1457915149,1458001000,1458957533; Hm_lpvt_9c7f4d9b7c00cb5aba2c637c64a41567=1459236059',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'smth_spider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'smth_spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'smth_spider.pipelines.DuplicatesPipeline': 300,
   'smth_spider.pipelines.MongoPipeline': 500,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
