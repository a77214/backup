### 验证登录
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

# 初始化 WebDriver
driver = webdriver.Chrome()
# 目标网址
target_url = "https://www.bilibili.com"
# 打开目标网站
driver.get(target_url)

# 加载 Cookies
cookies_path = "bilibili_cookies.pkl"
with open(cookies_path, 'rb') as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

# 刷新页面以验证登录
driver.refresh()
time.sleep(10)

# 关闭浏览器
driver.quit()