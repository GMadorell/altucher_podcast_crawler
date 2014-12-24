# -*- coding: utf-8 -*-

# Scrapy settings for altucher_podcast_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'altucher_podcast_scraper'

SPIDER_MODULES = ['altucher_podcast_scraper.spiders']
NEWSPIDER_MODULE = 'altucher_podcast_scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'altucher_podcast_scraper (+http://www.yourdomain.com)'
ITEM_PIPELINES = {#'altucher_podcast_scraper.pipelines.PickOnlyAskPodcastsPipeline': 1,
                  'altucher_podcast_scraper.pipelines.NameSimplifierPipeline': 2,
                  'altucher_podcast_scraper.pipelines.DownloadPodcastsPipeline': 3
                  }