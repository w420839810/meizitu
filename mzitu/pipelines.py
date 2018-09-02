# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline

class OverFilePipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        str = request.url.split('/')

        if len(str) >= 3:
            filename = str[-1]
            fileyear = str[-3]
            filemonth = str[-2]
        else:
            filename = str[-1]

        if '.' not in filename:
            filename  = filename +'.png'
        if len(str) >= 3:
            return '%s/%s/%s'% (fileyear ,filemonth ,filename)
        else:
            return '%s' % filename

        # filename = request.url.split('/')[-1]
        # if '.' not in filename:
        #     filename = filename + '.png'
        # print(filename, '***' * 30)
        # return 'pexels/%s' % filename
        # https://www.pexels.com/photo/filename.jpeg


class MzituPipeline(object):
    def process_item(self, item, spider):
        tmp = item['file_urls']
        item['file_urls'] = []
        for i in tmp:
            if 'thumbs' in i:
                print(i)
            else:
                item['file_urls'].append(i)
        return item
