# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImoveisCrawlingItem(scrapy.Item):
    id = scrapy.Field()
    titulo = scrapy.Field()
    regiao = scrapy.Field()
    detalhes = scrapy.Field()
    preco = scrapy.Field()
    data_de_publicacao = scrapy.Field()
