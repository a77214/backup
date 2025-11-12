import pickle
import time
from io import BytesIO

import pytesseract
import cv2
import numpy as np
import pyautogui
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait

from chaojiying import Chaojiying_Client
from kuai import base64_api

# 配置 Tesseract OCR 路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows 示例路径

# 初始化 WebDriver
driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/blackboard/new-award-exchange.html?task_id=6ERA3wloghveyo00")
cookies_path = "bilibili_cookies.pkl"

with open(cookies_path, 'rb') as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

# 定期刷新页面并检查按钮状态
while True:

    driver.refresh()  # 刷新页面
    time.sleep(5)  # 每 5 秒刷新一次

    try:
        # 通过 JavaScript 检查按钮是否为灰色并移除 disable 类
        driver.execute_script("""
            var button = document.querySelector('.exchange-button');
            if (button.classList.contains('disable')) {
                button.classList.remove('disable');  // 去掉 disable 类
            }
        """)

        # 查找按钮
        button = driver.find_element(By.CLASS_NAME, "exchange-button")

        # 如果按钮可点击
        if "disable" not in button.get_attribute("class"):
            print("按钮可点击，开始抢购!")
            button.click()  # 点击进行抢购\

        else:
            print("按钮为灰色，等待按钮变为可点击...")

        time.sleep(2)  # 等待按钮状态变更
    except Exception as e:
        print("按钮未找到或其他错误:", e)

    # 处理验证码
    try:
        print("111111111111")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'geetest_item_img'))
        )
        time.sleep(2)
        # 查找验证码图片
        captcha_img =driver.find_element(By.CSS_SELECTOR, 'body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_panelshowclick > div.geetest_panel_next > div')

        captcha_img.screenshot("captcha.png")
        a = base64_api(uname='a791075970', pwd='Aa791075970', img='captcha.png', typeid=27)
        print(a)
        location = captcha_img.location  # 获取元素左上角的坐标
        size = captcha_img.size  # 获取元素的宽度和高度
        left = captcha_img.location['x']
        top =captcha_img.location['y']
        right = captcha_img.location['x'] + captcha_img.size['width']
        down = captcha_img.location['y'] + captcha_img.size['height']
        im = Image.open('big.png')
        im = im.crop((left, top, right, down))
        im.save('yzm.png')
        https: // blog.csdn.net / weixin_35671421 / article / details / 113643301?ops_request_misc = %257
        B % 2522
        request % 255
        Fid % 2522 % 253
        A % 25223
        dc34f8a444259b596b1a91a508b06c6 % 2522 % 252
        C % 2522
        scm % 2522 % 253
        A % 252220140713.130102334.pc % 255
        Fall. % 2522 % 257
        D & request_id = 3
        dc34f8a444259b596b1a91a508b06c6 & biz_id = 0 & utm_medium = distribute.pc_search_result.none - task - blog - 2
        ~all
        ~first_rank_ecpm_v1
        ~rank_v31_ecpm - 4 - 113643301 - null - null
        .142 ^ v100 ^ pc_search_result_base7 & utm_term = b % E7 % AB % 99 % E9 % AA % 8
        C % E8 % AF % 81 % E7 % A0 % 81 & spm = 1018.2226
        .3001
        .4187
        # 在实际点击时使用元素的位置和大小校正坐标
        for result in a.split("|"):
            x, y = result.split(",")  # 获取 x 和 y 坐标
            x, y = int(x), int(y)  # 将坐标转换为整数

            # 校正坐标
            corrected_x = location['x'] + x  # 将相对坐标转换为页面坐标
            corrected_y = location['y'] + y  # 将相对坐标转换为页面坐标

            print(corrected_x, corrected_y)
            driver.execute_script("""
                let div = document.createElement('div');
                div.style.position = 'absolute';
                div.style.top = arguments[0] + 'px';
                div.style.left = arguments[1] + 'px';
                div.style.width = '10px';
                div.style.height = '10px';
                div.style.backgroundColor = 'red';
                div.style.borderRadius = '50%';
                div.style.zIndex = '9999';
                div.style.transition = 'all 0.2s ease-in-out';  // 添加动画效果
                document.body.appendChild(div);
            """, x, y)

            # 模拟点击
            ActionChains(driver).move_to_element(captcha_img).move_by_offset(x, y).click().perform()
            time.sleep(10)

    except Exception as e:
        print("验证码捕获失败或没有显示:", e)

    time.sleep(5)  # 每次检查间隔时间






# import requests
#
# # 请求头信息
# data = {
#     "referer": "https://www.bilibili.com/blackboard/new-award-exchange.html?task_id=6ERA3wloghvqhi00",
#     "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"Windows"',
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
# }
#
# # 发送 GET 请求
# url = "https://www.bilibili.com/blackboard/new-award-exchange.html?task_id=6ERA3wloghvqhi00"
# response = requests.get(url, headers=data)
# # 保存验证码图像
# with open("captcha.png", "wb") as f:
#     f.write(response.content)