import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    option = webdriver.EdgeOptions()
    # 设置无头模式，避免了打开浏览器页面
    option.add_argument('headless')
    chrome_options = Options()
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
        "cookie=gr_user_id=248ef70f-0416-41b7-9e6e-9dba1648c777; NOWCODERCLINETID=855661FAAB69093FBB51246933B64D49; __snaker__id=S8HK1Ho06T2oFl82; c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=485873428; _bl_uid=qImvX0IzuytrjyqpkeR8uIR3hU5p; NOWCODERUID=64A59DC224CD63C158D8A5B2D8A5C6CD; isAgreementChecked=true; Hm_lvt_a808a1326b6c06c437de769d1b85b870=1734162329,1734397607; HMACCOUNT=36B6EB6AF8653D21; csrfToken=VFRfBorY8qY6ZdINB3Ie-UoW; gdxidpyhxdE=vTHysQ5dnHmX3DQDVw7TSSNM6t8qBiE614A1m8ro5LfDeNpZ8YPNG%2BTJA5QxPaS%5CWg%2FIGpZiK6QMRhwmUV35lIBrTvnwadCXQTO1B7HjD6C4IqIxjafdrfaHYeDT%2B7h%5C23u0v8vVcOhY5SC%2B5DmefzL2YhgZlxvL2aocb6EqJeYwdRfk%3A1734513030456; t=8162BD84ECEB185B0CFAE772FA8769DB; username=a77a; username.sig=mMgGfQ9PdV0GfAsa5_qgA1vBf0x0nAPAnjn5FqkBTmY; uid=485873428; uid.sig=x6Mh7uMTYsGhJJ3J_Kpp5FDe-lEL--gXEL5oKJKpemY; c196c3667d214851b11233f5c17f99d5_gr_session_id=f0b8eaf6-0b8a-442c-b765-2135d1e6b428; c196c3667d214851b11233f5c17f99d5_gr_last_sent_sid_with_cs1=f0b8eaf6-0b8a-442c-b765-2135d1e6b428; c196c3667d214851b11233f5c17f99d5_gr_session_id_f0b8eaf6-0b8a-442c-b765-2135d1e6b428=true; acw_tc=6d33b0303faf7f5062fe970f2beab2344ae360673017d89740f10bc87dc1ae52; SERVERID=4dbe79c1d238e309c92410f93a7c85d4|1734664830|1734664830; SERVERCORSID=4dbe79c1d238e309c92410f93a7c85d4|1734664830|1734664830; c196c3667d214851b11233f5c17f99d5_gr_cs1=485873428; Hm_lpvt_a808a1326b6c06c437de769d1b85b870=1734664833"
    )

    # 这里使用了我之前登录过的浏览器
    browser =  webdriver.Chrome(options=option)
    browser.get("https://www.nowcoder.com/np-api/u/job/square-search?_=1734664834190")
    while True:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@class="job-card-item"]'))
        )


        jobs=browser.find_element(By.XPATH,'//div[@class="job-card-item"]//span[@class="job-name"]')
        print(1111111)

        print(jobs.text)
        print(22222)

