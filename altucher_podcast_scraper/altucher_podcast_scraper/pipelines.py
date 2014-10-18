# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
from scrapy.exceptions import DropItem


class PickOnlyAskPodcastsPipeline(object):

    def process_item(self, item, spider):
        if "ask altucher" not in unicode(item["name"]).lower():
            raise DropItem("Not a ask podcast")
        else:
            return item


class NameSimplifierPipeline(object):
    def process_item(self, item, spider):
        name = \
            item["name"]\
            .encode("ascii", "ignore")\
            .strip("\n")\
            .replace("?", "")\
            .replace('"', "")

        item["name"] = name
        return item

class DownloadPodcastsPipeline(object):
    def process_item(self, item, spider):
        link = item["download_link"]

        if not os.path.exists("download"):
            os.makedirs("download")

        name = item["name"].encode("ascii", "ignore").strip("\n")

        file_name = os.path.join("download", "{}.mp3".format(name))

        if os.path.exists(file_name):
            raise DropItem("Already downloaded ({})".format(file_name))

        r = requests.get(link)
        with open(file_name, "wb") as fd:
            fd.write(r.content)

        return item


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item
