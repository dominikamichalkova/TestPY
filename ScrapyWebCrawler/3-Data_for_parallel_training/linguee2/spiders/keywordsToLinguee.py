# -*- coding: utf-8 -*-
import scrapy, re, urllib
from linguee2.items import Linguee2Item

class LingueeSpider(scrapy.Spider):
    name = 'keywordstolinguee'
    allowed_domains = ['linguee.com', 'thefreedictionary.com', 'articles.bplans.com']
    start_urls = ['http://legal-dictionary.thefreedictionary.com/',
                  'http://financial-dictionary.thefreedictionary.com/',
                  'http://articles.bplans.com/business-term-glossary/'
                  ]

    def parse(self, response):
        # Gets keywords from thefreedictionary
        if response.request.meta['download_slot'] == 'legal-dictionary.thefreedictionary.com'\
                or response.request.meta['download_slot'] == 'financial-dictionary.thefreedictionary.com':
            for text in response.css('td > a::text'):
                extracted_text = text.extract().strip().encode('utf-8')
                # Takes care of special URL characters
                extracted_text = urllib.quote(extracted_text, safe='')
                # In URL there is + in place of a space
                pattern = r'%20'
                extracted_text = re.sub(pattern, '+', extracted_text)
                url = 'http://www.linguee.com/english-spanish/search?source=auto&query='+str(extracted_text)
                yield scrapy.Request(url, callback=self.parse)
        # Gets keywords from bplans (Business Term Glossary)
        elif response.request.meta['download_slot'] == 'articles.bplans.com':
            for text in response.css('li > a::text'):
                extracted_text = text.extract().strip().encode('utf-8')
                if extracted_text:
                    # Takes care of special URL characters
                    extracted_text =  urllib.quote(extracted_text, safe='')
                    # In URL there is + in place of a space
                    pattern = r'%20'
                    extracted_text = str(re.sub(pattern, '+', extracted_text))
                    url = 'http://www.linguee.com/english-spanish/search?source=auto&query='+str(extracted_text)
                    yield scrapy.Request(url, callback=self.parse)
        # Parses translation pairs on linguee
        else:
            remove_html_tags_pattern = r"<(?:[^>=]|='[^']*'|=\"[^\"]*\"|=[^\'\"][^\s>]*)*>|\r\n|\[\.\.\.\]|:"
            remove_link_pattern = r'<div[^>]*class="(behindLinkDiv|source_url|source_url_spacer)"[^>]*>(.*?)</div>'
            for text in response.css('tr'):
                # Gets rid of HTML elements with links
                en_text_wo_link = re.sub(remove_link_pattern, '', text.css('td.sentence.left').extract_first())
                es_text_wo_link = re.sub(remove_link_pattern, '', text.css('td.sentence.right2').extract_first())
                # Gets rid of HTML tags
                en_text = re.sub(remove_html_tags_pattern, '', en_text_wo_link).encode('utf-8')
                es_text = re.sub(remove_html_tags_pattern, '', es_text_wo_link).encode('utf-8')
                # Merges multiple spaces
                en_text = str(' '.join(en_text.split()))
                es_text = str(' '.join(es_text.split()))
                item = Linguee2Item()
                item['Linguee'] = yield {
                    'English': en_text,
                    'Spanish': es_text
                }
