# -*- coding: utf-8 -*-
import scrapy, re
from linguee2.items import Linguee2Item

class LingueeSpider(scrapy.Spider):
    name = 'linguee'
    allowed_domains = ['linguee.com']
    start_urls = ['http://www.linguee.com/english-spanish/search?source=auto&query=contract']

    def parse(self, response):
        pattern = r"<(?:[^>=]|='[^']*'|=\"[^\"]*\"|=[^\'\"][^\s>]*)*>|\r\n|\[\.\.\.\]"
        for text in response.css('tr'):
            item = Linguee2Item()
            item['Linguee'] = yield {
                'English': re.sub(pattern, '', text.css('td.sentence.left').extract()[0]),
                'Spanish': re.sub(pattern, '', text.css('td.sentence.right2').extract()[0]),
            }
