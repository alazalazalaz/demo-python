from selenium import webdriver
from selenium.common import exceptions as CE
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import requests
import cv2
import numpy as np
from cal_distance import get_track2 as trace_func
import random
import re


STATUS_NORMAL = 0   # 正常状态
STATUS_VERIFY = 1   # 需要验证码状态
STATUS_LIMIT = 2   # 频次限制状态
VERIFY_RETRY = 3    # 验证码重试次数
USE_SLIDER_IMG_CACHE = False    # 是否使用滑块图片缓存(缓存是指计算好了x值)

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


def get_slider_move_xy(bg_img_path, front_img_path, temp_img_path, result_img_path=""):
    # 输入图片，获取匹配的结果，返回数组[x, y]
    bg_img = cv2.imread(bg_img_path)
    front_img = cv2.imread(front_img_path)

    bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    bg_img = abs(255 - bg_img)
    cv2.imwrite(temp_img_path, bg_img)
    bg_img = cv2.imread(temp_img_path)
    result = cv2.matchTemplate(bg_img, front_img, cv2.TM_CCOEFF_NORMED)
    y, x = np.unravel_index(result.argmax(), result.shape)

    # 结果写入一张图片
    if result_img_path != "":
        cv2.rectangle(bg_img, (x, y), (x + 10, y + 10), (7, 249, 151), 2)
        cv2.imwrite(result_img_path, bg_img)

    return [x, y]


def is_return_data():
    # 检查是否返回数据slider_bg_timeout_sec = 5
    #
    #     try:
    #         WebDriverWait(driver, slider_bg_timeout_sec).until(
    #             EC.presence_of_element_located((By.ID, "tcaptcha_iframe"))
    #         )
    #     except CE.TimeoutException:
    #         print("等待{}s后未发现tcaptcha_iframe元素\r\n".format(slider_bg_timeout_sec))
    #         return False

    return True


def is_need_verify():
    # 检查是否需要验证码
    slider_bg_timeout_sec = 5

    try:
        WebDriverWait(driver, slider_bg_timeout_sec).until(
            EC.presence_of_element_located((By.ID, "tcaptcha_iframe"))
        )
    except CE.TimeoutException:
        print("等待{}s后未发现tcaptcha_iframe元素\r\n".format(slider_bg_timeout_sec))
        return False
    
    return True


def do_verify():
    handle = driver.current_window_handle

    xy = _handle_img_xy()
    x = xy[0]

    # driver.switch_to.default_content()  # 切回主DOM
    # driver.switch_to.window(handle)

    # _handle_slider_move(x)

    return False


def _handle_img_xy():
    driver.switch_to.frame("tcaptcha_iframe")  # 切换到iframe DOM

    # 获取两张图片地址
    bg_img = driver.find_element_by_id("slideBg").get_attribute("src")
    front_img = driver.find_element_by_id("slideBlock").get_attribute("src")
    @todo从这里才是测试
    print("北京图片：{}\r\n{}".format(bg_img, front_img))
    exit()

    # 计算出图片后缀
    img_index_and_sub_sid = _get_slider_subsid(bg_img)
    img_index = img_index_and_sub_sid[0]
    sub_sid = img_index_and_sub_sid[1]

    # 生成图片本地地址
    t = _date()
    bg_img_path = _get_slider_img_bg_path(sub_sid, img_index, t)
    front_img_path = _get_slider_img_front_path(sub_sid, img_index, t)
    temp_img_path = _get_slider_img_temp_path(sub_sid, img_index, t)
    result_img_path = _get_slider_img_temp_path(sub_sid, img_index, t)

    # 抓取图片并保存
    r = requests.get(bg_img)
    with open(bg_img_path, 'wb') as f:
        f.write(r.content)

    # 抓取图片并保存
    r = requests.get(front_img)
    with open(front_img_path, 'wb') as f:
        f.write(r.content)

    # 计算图片匹配结果，获取xy
    xy_array = get_slider_move_xy(bg_img_path, front_img_path, temp_img_path, result_img_path)
    x = xy_array[0]
    y = xy_array[1]
    print("获取滑块位置：x={}, y={}".format(x, y))
    return xy_array


def _handle_slider_move(x):
    # 拖动滑块
    slider_button = driver.find_element_by_id("tcaptcha_drag_button")
    ActionChains(driver).click_and_hold(slider_button).perform()
    time.sleep(random.randint(5, 10) / 10)
    total = int(x / 2 - 27.5) + 2
    track_array = trace_func(total)
    for i in track_array:
        ActionChains(driver).move_by_offset(i, 0).perform()
    print(len(track_array))
    print(track_array)
    time.sleep(random.randint(5, 10) / 10)
    ActionChains(driver).release().perform()
    print("拖动完成\r\n")


# @todo 设计一个方法把识别过的图片保存起来，下次直接读取识别后的数据，甚至都可以不用下载图片
# @todo 前提是验证好subsid和图片是否有关联
def _get_slider_subsid(img_path):
    phone_preg = re.compile("img_index=(\d)&subsid=(\d+)")
    result = phone_preg.findall(img_path)
    img_index = result[0][0]
    subsid = result[0][1]
    return [img_index, subsid]


def _get_slider_img_dir_path():
    return "./img/slider/".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def _get_slider_img_bg_path(subsid, img_index, t):
    return "./img/slider/{}_{}_{}_bg.jpeg".format(subsid, img_index, t)


def _get_slider_img_front_path(subsid, img_index, t):
    return "./img/slider/{}_{}_{}_front.png".format(subsid, img_index, t)


def _get_slider_img_temp_path(subsid, img_index, t):
    return "./img/slider/{}_{}_{}_temp.png".format(subsid, img_index, t)


def _get_slider_img_result_path(subsid, img_index, t):
    return "./img/slider/{}_{}_{}_result.png".format(subsid, img_index, t)


def collect_data():
    return True


def main():
    click_search()

    # 判断状态，状态有三种，1、正常返回，2、验证码，3、频次限制
    if is_return_data():    # 判断是否返回数据
        collect_data()
        # continue

    if is_need_verify():   # 判断是否需要验证码
        for i in range(VERIFY_RETRY):
            if do_verify():
                break


def _date():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


if __name__ == "__main__":
    main()


# assert "no result found" not in driver.page_source
# driver.close()    # 关闭当前tab
# driver.quit()     # 关闭整个浏览器


