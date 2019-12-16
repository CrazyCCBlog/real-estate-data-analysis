# -*- coding: utf-8 -*-
import scrapy
from imoveis_crawling.items import ImoveisCrawlingItem
import time
import random


class ImoveisCrawlingSpider(scrapy.Spider):
    name = 'IMOVEIS'
    allowed_domains = ['olx.com.br']
    page_number = 1

    def __init__(self, category="aluguel", region=None, state=None, *args, **kwargs):
        super(ImoveisCrawlingSpider, self).__init__(*args, **kwargs)
        self.category = category
        self.region = region
        self.state = state
        self.start_urls = ['https://%s.olx.com.br/%s/imoveis/%s?sf=1' % (self.state, self.region, self.category)]

    def parse(self, response):

        for item in response.css("a.OLXad-list-link "):
            id = item.css("::attr(name)").extract_first()
            titulo = item.css("::attr(title)").extract_first()
            regiao = item.css("div.OLXad-list-line-2 p.text.detail-region ::text").extract_first()
            detalhes = item.css("div.OLXad-list-line-1 p ::text").extract_first()
            preco = item.css("p.OLXad-list-price ::text").extract_first()
            data_de_publicacao = item.css("p.text.mb5px ::text").extract_first()

            imovel = ImoveisCrawlingItem(id=id, titulo=titulo, regiao=regiao, detalhes=detalhes, preco=preco,
                                         data_de_publicacao=data_de_publicacao)
            yield imovel

        time.sleep(random.randint(15, 20))
        self.page_number += 1

        if self.page_number < 70:
            next_page = self.start_urls[0] + '&o=' + str(self.page_number)
            yield scrapy.Request(next_page, callback=self.parse)
