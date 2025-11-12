import datetime
import json
import time

import scrapy
from scrapy import Selector
from scrapy.http import HtmlResponse
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from zhao.items import ZhaoItem


class NiukeSpider(scrapy.Spider):
    name = "niuke"
    allowed_domains = ["www.nowcoder.com"]
    # start_urls = [
    #     "https://www.nowcoder.com/jobs/fulltime/center?recruitType=3&city=%E5%8C%97%E4%BA%AC&city=%E4%B8%8A%E6%B5%B7&city=%E5%B9%BF%E5%B7%9E&city=%E6%B7%B1%E5%9C%B3&city=%E6%9D%AD%E5%B7%9E&city=%E6%88%90%E9%83%BD&city=%E6%AD%A6%E6%B1%89&careerJob=11002"
    # ]
    def __init__(self, *args, **kwargs):
        super(NiukeSpider, self).__init__(*args, **kwargs)
        self.page = 1  # 从第一页开始
        self.visited_jobs = set()  # 用于存储已访问的招聘数据（比如通过ID或其他唯一字段）
        self.previous_page_data = None  # 用于保存上一页的数据

    def start_requests(self):
        url = "https://www.nowcoder.com/np-api/u/job/square-search?_=1734673993201"

        while True:
            data = {
                "requestFrom": "1",
                "page": str(self.page),  # 使用当前的page
                "pageSize": "20",
                "recruitType": "3",
                "pageSource": "5001",
                "jobCity": "北京, 上海, 广州, 深圳, 杭州",
                "careerJobId": "11014",
                "visitorId": "82f1163f-52a9-421e-9e13-062bdd9ce709"
            }

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Cookie": "gr_user_id248ef70f-0416-41b7-9e6e-9dba1648c777; NOWCODERCLINETID=855661FAAB69093FBB51246933B64D49; __snaker__id=S8HK1Ho06T2oFl82; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=485873428; _bl_uid=qImvX0IzuytrjyqpkeR8uIR3hU5p; NOWCODERUID=64A59DC224CD63C158D8A5B2D8A5C6CD; isAgreementChecked=true; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1734162329,1734397607; HMACCOUNT=36B6EB6AF8653D21; csrfToken=VFRfBorY8qY6ZdINB3Ie-UoW; gdxidpyhxdE=vTHysQ5dnHmX3DQDVw7TSSNM6t8qBiE614A1m8ro5LfDeNpZ8YPNG%2BTJA5QxPaS%5CWg%2FIGpZiK6QMRhwmUV35lIBrTvnwadCXQTO1B7HjD6C4IqIxjafdrfaHYeDT%2B7h%5C23u0v8vVcOhY5SC%2B5DmefzL2YhgZlxvL2aocb6EqJeYwdRfk%3A1734513030456; t=8162BD84ECEB185B0CFAE772FA8769DB; username=a77a; username.sig=mMgGfQ9PdV0GfAsa5_qgA1vBf0x0nAPAnjn5FqkBTmY; uid=485873428; uid.sig=x6Mh7uMTYsGhJJ3J_Kpp5FDe-lEL--gXEL5oKJKpemY; c196c3667d214851b11233f5c17f99d5_gr_session_id=f0b8eaf6-0b8a-442c-b765-2135d1e6b428; c196c3667d214851b11233f5c17f99d5_gr_last_sent_sid_with_cs1=f0b8eaf6-0b8a-442c-b765-2135d1e6b428; c196c3667d214851b11233f5c17f99d5_gr_session_id_f0b8eaf6-0b8a-442c-b765-2135d1e6b428=true; acw_tc=6d33b0303faf7f5062fe970f2beab2344ae360673017d89740f10bc87dc1ae52; SERVERID=4dbe79c1d238e309c92410f93a7c85d4|1734664830|1734664830; SERVERCORSID=4dbe79c1d238e309c92410f93a7c85d4|1734664830|1734664830; c196c3667d214851b11233f5c17f99d5_gr_cs1=485873428; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1734664833"
            }
            print(f"at the{self.page}页")
            # 发送请求
            yield scrapy.FormRequest(url=url, callback=self.parse, formdata=data, headers=headers)
            # 增加 page 参数，继续下一页
            self.page += 1

    def parse(self, response):
        content = response.text
        obj = json.loads(content)

        # 获取当前页的招聘信息
        current_page_data = obj.get('data', [])
        data = obj.get("data", {})
        total_count = data.get("totalCount", 0)
        total_page = data.get("totalPage", 0)
        current_page = data.get("currentPage", 0)

        print(f"Total count: {total_count}, Total pages: {total_page}, Current page: {current_page}")

        # 获取每一条招聘信息
        job_list = data.get("datas", [])


        job_data = obj.get("data", {})

        # 创建 Item 实例
        item = ZhaoItem()

        item['job_name'] = job_data.get('jobName', '')
        item['job_city'] = job_data.get('jobCity', '')
        item['salary_min'] = job_data.get('salaryMin', 0)
        item['salary_max'] = job_data.get('salaryMax', 0)
        item['salary_month'] = job_data.get('salaryMonth', 0)
        item['job_keys'] = job_data.get('jobKeys', '')

        # 解析 ext 字段
        ext_data = json.loads(job_data.get('ext', '{}'))
        item['job_requirements'] = ext_data.get('requirements', '')
        item['job_infos'] = ext_data.get('infos', '')
        item['job_strength'] = ext_data.get('jobStrength', '')

        # 时间戳转化
        item['create_time'] = self.timestamp_to_datetime(job_data.get('createTime'))
        item['update_time'] = self.timestamp_to_datetime(job_data.get('updateTime'))

        # 提取 tags（title）
        tags = []
        for tag in job_data.get('pcTagInfo', {}).get('jobInfoTagList', []):
            tag_title = tag.get('tag', {}).get('title', '')
            if tag_title:
                tags.append(tag_title)

        item['tags'] = tags  # 存储 tags 中的 title

        # 提取公司名称
        company_name = job_data.get('recommendInternCompany', {}).get('companyName', '')
        item['company_name'] = company_name

        # 判断当前页的数据是否与上一页重复
        if self.previous_page_data is not None and self.previous_page_data == current_page_data:
            self.log("Duplicate data found between current and previous page, stopping the crawl.")
            self.crawler.engine.close_spider(self, reason="Duplicate data found between pages")
            return  # 如果当前页的数据与上一页相同，则停止爬取

        # 保存当前页的数据作为上一页数据
        self.previous_page_data = current_page_data

        # 处理当前页的数据（假设我们保存每一页的内容）
        yield item

        def timestamp_to_datetime(self, timestamp):
            """将时间戳转换为日期时间格式"""
            if timestamp:
                return datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
            return None

    # def __init__(self):
    #
    #     # 设置 Selenium WebDriver
    #     chrome_options = Options()
    #     chrome_options.add_argument("--headless")  # 不打开浏览器界面
    #
    #     chrome_options.add_argument('--ignore-certificate-errors')
    #     # 忽略 Bluetooth: bluetooth_adapter_winrt.cc:1075 Getting Default Adapter failed. 错误
    #     chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    #     # 忽略 DevTools listening on ws://127.0.0.1... 提示
    #     chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #
    #     self.driver = webdriver.Chrome(options=chrome_options)
    #
    # def parse(self, response):
    #
    #     self.driver.get(response.url)
    #     time.sleep(5)
    #     js_button = "document.documentElement.scrollTop=10000"
    #     self.driver.execute_script(js_button)
    #
    #     # 等待 JavaScript 渲染完成
    #     self.driver.implicitly_wait(10)
    #
    #     # 获取渲染后的 HTML
    #     rendered_html = self.driver.page_source
    #     # 使用 Scrapy 的 HtmlResponse 解析渲染后的 HTML
    #     response = HtmlResponse(url=self.driver.current_url, body=rendered_html, encoding='utf-8')
    #
    #
    #     # 提取数据
    #     time.sleep(5)
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located(
    #             (By.XPATH, '//div[@class="job-card-item"]'))
    #     )
    #     print(111111111)
    #
    #     # 在这里处理页面内容
    #     list = response.xpath('//div[@class="job-card-item"]')
    #
    #
    #     print(list.getall())