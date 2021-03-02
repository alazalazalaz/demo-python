from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import requests
import cv2
import numpy as np


STATUS_NORMAL = 0   # 正常状态
STATUS_VERIFY = 1   # 需要验证码
STATUS_LIMIT = 2   # 频次限制

driver = webdriver.Chrome()
driver.get("https://www.luckyair.net/flight/search.html")


def click_search():
    # 点击搜索按钮
    time.sleep(10)
    # 等待可点击
    # try:
    #     element = WebDriverWait(driver, timeout_sec).until(
    #         EC.presence_of_element_located((By.XPATH, "//input[@placeholder='出发城市']"))
    #     )
    # finally:
    #     print("等待{}s后未发现元素\r\n".format(timeout_sec))
    # driver.quit()

    assert "祥鹏" in driver.title  # 判断标题中是否含有Python，如果没有，则终止
    # 出发
    from_city_input = driver.find_element_by_xpath("//input[@placeholder='出发城市']")
    from_city_input.clear()  # 清空input
    from_city_input.send_keys("KMG")  # 输入pycon到input
    time.sleep(0.5)
    from_city_input.send_keys(Keys.RETURN)  # 回车

    # 到达
    to_city_input = driver.find_element_by_xpath("//input[@placeholder='到达城市']")
    to_city_input.clear()  # 清空input
    to_city_input.send_keys("CTU")  # 输入pycon到input
    time.sleep(0.5)
    to_city_input.send_keys(Keys.RETURN)  # 回车

    # 搜索
    search_button = driver.find_element_by_xpath("//button[@type='button']")
    search_button.send_keys(Keys.RETURN)


def get_slider_move_xy(bg_img_path, front_img_path, temp_img):
    bg_img = cv2.imread(bg_img_path)
    front_img = cv2.imread(front_img_path)

    bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    bg_img = abs(255 - bg_img)
    cv2.imwrite(temp_img, bg_img)
    bg_img = cv2.imread(temp_img)
    result = cv2.matchTemplate(bg_img, front_img, cv2.TM_CCOEFF_NORMED)
    y, x = np.unravel_index(result.argmax(), result.shape)
    return [x, y]


def check_search_status_normal():
    # 检查是否返回数据
    return True


def check_search_status_verify():
    # 检查是否需要验证码
    slider_bg_timeout_sec = 8
    time.sleep(slider_bg_timeout_sec)

    driver.switch_to.frame("tcaptcha_iframe")   # 切换到iframe DOM

    # 获取背景图
    bg_img = driver.find_element_by_id("slideBg").get_attribute("src")
    bg_img_path = "./img/bg_img.jpeg"
    r = requests.get(bg_img)
    with open(bg_img_path, 'wb') as f:
        f.write(r.content)

    # 获取背景图
    front_img = driver.find_element_by_id("slideBlock").get_attribute("src")
    front_img_path = "./img/front_img.png"
    r = requests.get(front_img)
    with open(front_img_path, 'wb') as f:
        f.write(r.content)

    xy_array = get_slider_move_xy(bg_img_path, front_img_path, "./img/temp.jpg")
    print(xy_array)
    exit()
    # driver.switch_to.default_content()  # 切回主DOM

    try:
        element = WebDriverWait(driver, slider_bg_timeout_sec).until(
            EC.presence_of_element_located((By.ID, "slideBg"))
        )
    finally:
        print("等待{}s后未发现slider背景元素\r\n".format(slider_bg_timeout_sec))
        driver.quit()
        exit()

    print("oooooooo")


def collect_data():
    return True


def main():
    click_search()

    # 判断状态，状态有三种，1、正常返回，2、验证码，3、频次限制
    if check_search_status_normal():    # 判断是否返回数据
        collect_data()
        # continue

    check_search_status_verify()   # 判断是否需要验证码


if __name__ == "__main__":
    main()


# assert "no result found" not in driver.page_source
# driver.close()    # 关闭当前tab
# driver.quit()     # 关闭整个浏览器


