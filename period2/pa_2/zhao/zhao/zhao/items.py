# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    job_name = scrapy.Field()       # 职位名称
    job_city = scrapy.Field()       # 工作城市
    salary_min = scrapy.Field()     # 最低薪资
    salary_max = scrapy.Field()     # 最高薪资
    salary_month = scrapy.Field()   # 薪资（月薪）
    job_keys = scrapy.Field()       # 技能要求
    job_requirements = scrapy.Field()  # 岗位要求
    job_address = scrapy.Field()    # 工作地址
    company_name = scrapy.Field()   # 公司名称
    user_nickname = scrapy.Field()  # 用户昵称
    user_gender = scrapy.Field()    # 用户性别
    tags = scrapy.Field()           # 职位标签