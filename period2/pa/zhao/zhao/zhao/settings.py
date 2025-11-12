# Scrapy settings for zhao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "zhao"

SPIDER_MODULES = ["zhao.spiders"]
NEWSPIDER_MODULE = "zhao.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "zhao (+http://www.yourdomain.com)"

# Obey robots.txt rules


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False


# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Cookie":"gr_user_id=248ef70f-0416-41b7-9e6e-9dba1648c777; NOWCODERCLINETID=855661FAAB69093FBB51246933B64D49; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=485873428; NOWCODERUID=64A59DC224CD63C158D8A5B2D8A5C6CD; isAgreementChecked=true; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1734162329,1734397607; HMACCOUNT=36B6EB6AF8653D21; t=8162BD84ECEB185B0CFAE772FA8769DB; username=a77a; username.sig=mMgGfQ9PdV0GfAsa5_qgA1vBf0x0nAPAnjn5FqkBTmY; uid=485873428; uid.sig=x6Mh7uMTYsGhJJ3J_Kpp5FDe-lEL--gXEL5oKJKpemY; c196c3667d214851b11233f5c17f99d5_gr_session_id=10bc144f-fbae-42df-b13d-5003e971fa23; c196c3667d214851b11233f5c17f99d5_gr_last_sent_sid_with_cs1=10bc144f-fbae-42df-b13d-5003e971fa23; c196c3667d214851b11233f5c17f99d5_gr_session_id_10bc144f-fbae-42df-b13d-5003e971fa23=true; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1734596427; c196c3667d214851b11233f5c17f99d5_gr_cs1=485873428"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "zhao.middlewares.ZhaoSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "zhao.middlewares.ZhaoDownloaderMiddleware": 543,
    'scrapy_selenium.SeleniumMiddleware': 800,
}
SELENIUM_DRIVER_NAME = 'chrome'  # 或者 'firefox'
SELENIUM_DRIVER_EXECUTABLE_PATH = None  # 留空使用 webdriver-manager 自动下载驱动
SELENIUM_DRIVER_ARGUMENTS = ['--headless']  # 无头模式

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "zhao.pipelines.ZhaoPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
