# -*- coding: utf-8 -*-
import scrapy
from imoveis_crawling.items import ImoveisCrawlingItem
import time
import random


class ImoveisCrawlingSpider(scrapy.Spider):
    name = 'IMOVEIS'
    allowed_domains = ['olx.com.br']

    def __init__(self, category="aluguel", region=None, state=None, *args, **kwargs):
        super(ImoveisCrawlingSpider, self).__init__(*args, **kwargs)
        self.category = category
        self.region = region
        self.state = state
        self.start_urls = ['https://%s.olx.com.br/%s/imoveis/%s?sf=1' % (self.state, self.region, self.category)]
        self.page_number = 1

    def parse(self, response):

        for item in response.css("a.fnmrjs-0.fyjObc"):
            id = item.css("::attr(data-lurker_list_id)").extract_first()
            titulo = item.css("h2.sc-1mbetcw-0.fKteoJ.sc-ifAKCX.jyXVpA ::text").extract_first()
            regiao = item.css("span.sc-7l84qu-1.ciykCV.sc-ifAKCX.dpURtf ::text").extract_first()
            detalhes = item.css("span.sc-1j5op1p-0.lnqdIU.sc-ifAKCX.eLPYJb ::text").extract_first()
            preco = item.css(" span.sc-ifAKCX.eoKYee ::text").extract_first()
            data_de_publicacao = item.css("span.wlwg1t-1.fsgKJO.sc-ifAKCX.eLPYJb ::text").extract_first()

            imovel = ImoveisCrawlingItem(id=id, titulo=titulo, regiao=regiao, detalhes=detalhes, preco=preco,
                                         data_de_publicacao=data_de_publicacao)
            yield imovel

        time.sleep(random.randint(5, 15))
        self.page_number += 1

        if self.page_number < 100:
            next_page = self.start_urls[0] + '&o=' + str(self.page_number)
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)
