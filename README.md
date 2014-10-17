# Altucher Podcast Downloader #

This repo consists of a crawler made to automatically download all podcasts from http://www.stansberryradio.com/James-Altucher/.

Built using [Scrapy](https://github.com/scrapy/scrapy), an awesome python crawling framework.

## How to use it ##
Look at the fabfile.

Basically, if you have fab installed, just run:

    fab crawl

The crawler can be configured to download only a certain type of podcasts. Look into pipelines.py and the variable ITEM_PIPELINES in settings.py.