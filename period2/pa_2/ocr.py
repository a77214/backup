from kuai import base64_api

a = base64_api(uname='a791075970', pwd='Aa791075970', img='captcha.png', typeid=27)
print(a)
for result in a.split("|"):
    x, y = result.split(",")  # 获取 x 和 y 坐标
    x, y = int(x), int(y)  # 将坐标转换为整数
    print(x, y)
