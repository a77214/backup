from datetime import datetime

import json

import scrapy

from zhao.items import ZhaoItem


class NiukeSpider(scrapy.Spider):
    name = "niuke"
    allowed_domains = ["www.nowcoder.com"]
    # start_urls = ["https://www.nowcoder.com/np-api/u/job/square-search?_=1734673993201"]

    def __init__(self, *args, **kwargs):
        super(NiukeSpider, self).__init__(*args, **kwargs)
        self.page = 1  # 从第一页开始
        self.visited_jobs = set()  # 用于存储已访问的招聘数据（通过jobId来唯一标识）
        self.previous_page_data = set()  # 用于保存上一页的招聘数据（通过jobId唯一标识）

    def timestamp_to_datetime(self, timestamp):
        """将时间戳转换为日期时间格式"""
        if timestamp:
            return datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
        return None

    def start_requests(self):
        # url = "https://www.nowcoder.com/np-api/u/job/square-search?_=1734673993201"
        url="https://www.nowcoder.com/np-api/u/job/square-search?_=1734954360364"

        while True:
            data = {
                "requestFrom": "1",
                "page": str(self.page),  # 当前页面
                "pageSize": "20",  # 每页显示的条数
                "recruitType": "3",  # 招聘类型
                "pageSource": "5001",  # 来源页面
                "jobCity": "北京, 上海, 广州, 深圳, 杭州",  # 将所有的 jobCity 合并为一个逗号分隔的字符串
                "careerJobId": "11002",  # 职位类别ID
                "visitorId": "82f1163f-52a9-421e-9e13-062bdd9ce709"  # 访客ID
            }

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Cookie": "gr_user_id248ef70f-0416-41b7-9e6e-9dba1648c777; NOWCODERCLINETID=855661FAAB69093FBB51246933B64D49; __snaker__id=S8HK1Ho06T2oFl82; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=485873428; _bl_uid=qImvX0IzuytrjyqpkeR8uIR3hU5p; NOWCODERUID=64A59DC224CD63C158D8A5B2D8A5C6CD; isAgreementChecked=true; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1734162329,1734397607; HMACCOUNT=36B6EB6AF8653D21; csrfToken=VFRfBorY8qY6ZdINB3Ie-UoW; gdxidpyhxdE=vTHysQ5dnHmX3DQDVw7TSSNM6t8qBiE614A1m8ro5LfDeNpZ8YPNG%2BTJA5QxPaS%5CWg%2FIGpZiK6QMRhwmUV35lIBrTvnwadCXQTO1B7HjD6C4IqIxjafdrfaHYeDT%2B7h%5C23u0v8vVcOhY5SC%2B5DmefzL2YhgZlxvL2aocb6EqJeYwdRfk%3A1734513030456; t=8162BD84ECEB185B0CFAE772FA8769DB; username=a77a; username.sig=mMgGfQ9PdV0GfAsa5_qgA1vBf0x0nAPAnjn5FqkBTmY; uid=485873428; uid.sig=x6Mh7uMTYsGhJJ3J_Kpp5FDe-lEL--gXEL5oKJKpemY; c196c3667d214851b11233f5c17f99d5_gr_session_id=f0b8eaf6-0b8a-442c-b765-2135d1e6b428; c196c3667d214851b11233f5c17f99d5_gr_last_sent_sid_with_cs1=f0b8eaf6-0b8a-442c-b765-2135d1e6b428; c196c3667d214851b11233f5c17f99d5_gr_session_id_f0b8eaf6-0b8a-442c-b765-2135d1e6b428=true; acw_tc=6d33b0303faf7f5062fe970f2beab2344ae360673017d89740f10bc87dc1ae52; SERVERID=4dbe79c1d238e309c92410f93a7c85d4|1734664830|1734664830; SERVERCORSID=4dbe79c1d238e309c92410f93a7c85d4|1734664830|1734664830; c196c3667d214851b11233f5c17f99d5_gr_cs1=485873428; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1734664833"
            }

            print(f"At page {self.page}")  # 打印当前页
            # 发送请求
            yield scrapy.FormRequest(url=url, callback=self.parse, formdata=data, headers=headers)
            # 增加 page 参数，继续下一页
            self.page += 1

    def parse(self, response):
        content = response.text
        obj = json.loads(content)

        # 获取当前页的招聘数据
        datas = obj.get('data', {}).get('datas', [])
        if isinstance(datas, list):
            # 获取当前页的招聘信息（假设每条招聘信息都有 id）
            current_page_data = {item['data']['id'] for item in datas if
                                 isinstance(item, dict) and isinstance(item.get('data', {}), dict)}
            print(f"Current Page Data: {current_page_data}")  # 打印当前页的招聘信息
        else:
            self.log("Data is not a list. Please check the response structure.")
            return  # 如果数据不是列表，则停止当前回调

        # 判断当前页的数据是否与上一页重复
        if self.previous_page_data is not None and current_page_data == self.previous_page_data:
            self.log("Duplicate data found between current and previous page, stopping the crawl.")
            self.crawler.engine.close_spider(self, reason="Duplicate data found between pages")
            return  # 结束当前的回调

        # 保存当前页的数据作为上一页数据
        self.previous_page_data = current_page_data

        # 处理当前页的数据
        data = obj.get("data", {})
        total_count = data.get("totalCount", 0)
        total_page = data.get("totalPage", 0)
        current_page = data.get("currentPage", 0)

        print(f"Total count: {total_count}, Total pages: {total_page}, Current page: {current_page}")

        # 获取每一条招聘信息
        job_data_list = obj.get('data', {}).get('datas', [])

        for job_item in job_data_list:
            job_data = job_item.get('data', {})


            # 处理职位数据
            yield {
                'job_name': job_data.get('jobName', '无职位名称'),
                'job_city': job_data.get('jobCity', '未知城市'),
                'salary_min': job_data.get('salaryMin', 0),
                'salary_max': job_data.get('salaryMax', 0),
                'salary_month': job_data.get('salaryMonth', 12),  # 默认按月计薪
                'job_keys': job_data.get('jobKeys', '无技能要求'),
                'job_requirements': job_data.get('jobRequirements', '无岗位要求'),
                'job_address': job_data.get('jobAddress', '未提供地址'),
                'company_name': self.get_company_name(job_data),
                'user_nickname': job_data.get('user', {}).get('nickname', '无昵称'),
                'user_gender': job_data.get('user', {}).get('gender', '未知'),
                'tags': self.get_tags(job_data),
            }

    def get_tags(self, job_data):
        # 获取标签
        tags = job_data.get('pcTagInfo', {}).get('jobInfoTagList', [])
        return [tag['tag']['title'] for tag in tags if tag.get('tag', {}).get('title')] or ['无标签']
    def get_company_name(self, job_data):
        # 从user -> identity -> companyName 获取公司名称
        identity_list = job_data.get('user', {}).get('identity', [])
        for identity in identity_list:
            company_name = identity.get('companyName')
            if company_name:
                return company_name
        return '无公司名称'  # 如果没有找到公司名称，返回默认值