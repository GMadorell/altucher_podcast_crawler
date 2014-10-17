from fabric.decorators import task
from fabric.operations import local


@task
def scrap():
    local("scrapy crawl AltucherTest -o items.json")
