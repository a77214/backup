# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    job_city = scrapy.Field()
    salary_min = scrapy.Field()
    salary_max = scrapy.Field()
    salary_month = scrapy.Field()
    job_keys = scrapy.Field()
    job_requirements = scrapy.Field()
    job_infos = scrapy.Field()
    job_strength = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    tags = scrapy.Field()  # 添加 tags 字段
    company_name = scrapy.Field()
