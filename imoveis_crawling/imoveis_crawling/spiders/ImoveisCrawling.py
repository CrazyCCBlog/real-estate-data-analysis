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

        for item in response.css("li.sc-1fcmfeb-2.ggOGTJ"):
            id = item.css("a ::attr(data-lurker_list_id)").extract_first()
            titulo = item.css("div.fnmrjs-8.kRlFBv ::text").extract_first()
            regiao = item.css("p.fnmrjs-13.hdwqVC ::text").extract_first()
            detalhes = item.css("p.jm5s8b-0.jDoirm ::text").extract_first()
            preco = item.css("p.fnmrjs-16.jqSHIm ::text").extract_first()
            data_de_publicacao = item.css("p.fnmrjs-19.eJIIxH ::text").extract_first()

            imovel = ImoveisCrawlingItem(id=id, titulo=titulo, regiao=regiao, detalhes=detalhes, preco=preco,
                                         data_de_publicacao=data_de_publicacao)
            yield imovel

        time.sleep(random.randint(15, 20))
        self.page_number += 1

        if self.page_number < 70:
            next_page = self.start_urls[0] + '&o=' + str(self.page_number)
            yield scrapy.Request(next_page, callback=self.parse)
