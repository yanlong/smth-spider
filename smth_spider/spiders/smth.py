# -*- coding: utf-8 -*-
import scrapy
from pprint import pprint
from scrapy.linkextractors import LinkExtractor
import urllib
import os
import time
class SmthSpider(scrapy.spiders.CrawlSpider):
    name = "smth"
    allowed_domains = ["m.newsmth.net", "www.newsmth.net"]
    start_urls = (
        'http://m.newsmth.net/board/CreditCard',
        'http://m.newsmth.net/board/CreditCard?p=2',
        'http://m.newsmth.net/board/CreditCard?p=3',
        'http://m.newsmth.net/board/CreditCard?p=4',
        'http://m.newsmth.net/board/CreditCard?p=5',
    )

    base_url='http://m.newsmth.net'
    rules = (
        # Rule(LinkExtractor(allow=('/', 'zhihu\.com/topic/'))),

    )
    def parse(self, response):
        posts = response.css('#m_main > ul > li > div:nth-child(1) > a')
        for p in posts:
            title = p.css('::text').extract_first()
            link = p.css('::attr(href)').extract_first()
            if u'浦发' in title and (u'ae' in title or u'AE' in title):
                # print '=============>'+title, link
                yield  scrapy.Request(self.base_url+link, callback=self.parse_post)

    def parse_post(self, response):
        reposts = response.css('#m_main > ul > li')
        title = response.css('#m_main > ul > li.f').extract_first()
        for rep in reposts:
            content = rep.css('div.sp::text').extract_first()
            user = rep.css('div > div > a:nth-child(2)::text').extract_first()
            if not content or not user:
                continue
            if content.startswith(u'站内') or content.startswith(u'求') or content.startswith(u'同求'):
                print user
                yield {'id': user, 'content': content}

        next_page = response.css('#m_main > div:nth-child(4) > form > a:nth-child(1)')
        if next_page.css('::text').extract_first() == u'下页':
            yield scrapy.Request(self.base_url+next_page.css('::attr(href)').extract_first(), callback=self.parse_post)


    def send_invitation(self, user):
        # if user != 'gomypig':
            # return '';
        user='yimufei'
        url='http://www.newsmth.net/nForum/mail/NULL/ajax_send.json'
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36' ,
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' ,
            'Accept': '*/*' ,
            'Cache-Control': 'no-cache' ,
            'X-Requested-With': 'XMLHttpRequest' ,
            'Cookie': 'main[UTMPUSERID]=gomypig; main[UTMPKEY]=73051396; main[UTMPNUM]=17059; main[PASSWORD]=%2503d%2500a2%2540%2526%250D%2516%250923%251Bu%2509%252C%250D%2522%2507Vg%2523%2504%250E; Hm_lvt_9c7f4d9b7c00cb5aba2c637c64a41567=1459236700; Hm_lpvt_9c7f4d9b7c00cb5aba2c637c64a41567=1459240287; main[XWJOKE]=hoho' ,
            'Connection': 'keep-alive' ,
            'Referer': 'http://www.newsmth.net/nForum/' ,
            'Cookie': '_ga=GA1.2.316291097.1429852824; Hm_lvt_7734e0ab76401586c0e18dc2feefc01b=1441631966; bfd_g=9de2782bcb754fd70000689300906e3054c9fda8; tma=88525828.7971704.1429693672137.1449543590241.1449629553140.142; tmd=2533.88525828.7971704.1429693672137.; main[UTMPUSERID]=gomypig; main[UTMPKEY]=28696048; main[UTMPNUM]=12483; main[PASSWORD]=%2503d%2500a2%2540%2526%250D%2516%250923%251Bu%2509%252C%250D%2522%2507Vg%2523%2504%250E; main[XWJOKE]=hoho; Hm_lvt_9c7f4d9b7c00cb5aba2c637c64a41567=1457776174,1457915149,1458001000,1458957533; Hm_lpvt_9c7f4d9b7c00cb5aba2c637c64a41567=1459236059' ,
            'Origin': 'http://www.newsmth.net' ,
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4' ,
            'Pragma': 'no-cache' ,
            'Accept-Encoding': 'gzip, deflate',
            'xxxx':'xxx',
        }
        data={
            'id':'buddywoody',
            'title':'Re%3A+%E6%B1%82%E4%B8%AA%E6%B5%A6%E5%8F%91ae%E7%99%BD%E7%9A%84%E6%8E%A8%E8%8D%90',
            'content':'%E6%B5%A6%E5%8F%91AE%E7%99%BD%E9%87%91%E5%8D%A1%E6%8E%A8%E8%8D%90%E9%93%BE%E6%8E%A5%EF%BC%9Ahttps%3A%2F%2Fecentre.spdbccc.com.cn%2Fentry_cobber_union%2FpageController%2FmySticker.htm%3Fcid%3D365746%0A%E3%80%90+%E5%9C%A8+buddywoody+%E7%9A%84%E5%A4%A7%E4%BD%9C%E4%B8%AD%E6%8F%90%E5%88%B0%3A+%E3%80%91%0A%3A+%2F%2Fbow%0A',
            'signature':'0',
            'backup':'on',
            'num':'',
        }
        os.system('bash smth_spider/spiders/send_invitation.sh '+user)

        # print urllib.urlencode(data)
        # req= scrapy.Request(url, method='POST', headers=headers, body=urllib.urlencode(data))
        # print dir(req.body)


