# -*- coding: utf-8 -*-
import json
from datetime import date
import os


class ImoveisCrawlingPipeline(object):

    file_obj = None

    def open_spider(self, spider):
        category = spider.category
        file = os.getcwd() + "/files/imoveis/{}/{}OLX_{}.txt".format(category, category, date.today())
        self.file_obj = open(file, "w")

    def close_spider(self, spider):
        self.file_obj.close()

    def process_item(self, item, spider):
        item['titulo'] = item['titulo'].replace("00e2", "â").replace("00e1", "á").replace('00e9', 'é').\
            replace('00f3', 'ó').replace('00e7', 'ç').replace('00e3', 'ã').replace('00ed', 'í').replace('\\u', '')
        item['regiao'] = item['regiao'].replace('\t', '').replace('\n', '').replace("00e2", "â").\
            replace("00e1", "á").replace('00e9', 'é').replace('00f3', 'ó').replace('00e7', 'ç').\
            replace('00e3', 'ã').replace('00ed', 'í').replace('\\u', '')
        item['detalhes'] = item['detalhes'].replace('\t', '').replace('\n', '').replace("00e2", "â").\
            replace("00e1", "á").replace('00e9', 'é').replace('00f3', 'ó').replace('00e7', 'ç').\
            replace('00e3', 'ã').replace('00ed', 'í').replace('\\u', '')

        line = json.dumps(dict(item)) + '\n'
        self.file_obj.write(line)
        return item
