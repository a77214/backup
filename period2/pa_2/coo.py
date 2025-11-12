# 登录
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

# 初始化 WebDriver
driver = webdriver.Chrome()

# 打开 Bilibili 登录页面
login_url = "https://passport.bilibili.com/login"
driver.get(login_url)

# 等待登录完成（若有验证码需手动处理）
time.sleep(30)  # 手动处理验证码和二次验证

# 检查是否登录成功
if "bilibili.com" in driver.current_url:
    print("登录成功，当前页面URL:", driver.current_url)
else:
    print("登录失败，请检查账号信息或验证码！")

# 保存 Cookies
cookies_path = "bilibili_cookies.pkl"
with open(cookies_path, 'wb') as file:
    pickle.dump(driver.get_cookies(), file)
    print("Cookies 已保存到:", cookies_path)

# 关闭浏览器
driver.quit()