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
import shutil


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


def is_need_verify(slider_bg_timeout_sec):
    # 检查是否需要验证码

    try:
        WebDriverWait(driver, slider_bg_timeout_sec).until(
            EC.presence_of_element_located((By.ID, "tcaptcha_iframe"))
        )
    except CE.TimeoutException:
        print("等待{}s后未发现tcaptcha_iframe元素\r\n".format(slider_bg_timeout_sec))
        return False
    
    return True


def do_verify(i):
    # 验证验证码，即滑动滑块
    handle = driver.current_window_handle
    driver.switch_to.frame("tcaptcha_iframe")  # 切换到iframe DOM

    xy_and_img_local_path = _handle_img_xy()
    x = xy_and_img_local_path['xy'][0]
    # test data
    # if i == 0:
    #     x = 100

    _handle_slider_move(x)
    # driver.switch_to.default_content()  # 切回主DOM
    driver.switch_to.window(handle)
    return xy_and_img_local_path


def record_failed_img(xy_and_img_local_path):
    # 移动验证失败的图片到指定目录
    for i in range(len(xy_and_img_local_path['img_path'])):
            shutil.move(xy_and_img_local_path['img_path'][i], "./img/slider/error_img")

    return True


def refresh_verify():
    # 刷新验证码
    handle = driver.current_window_handle
    driver.switch_to.frame("tcaptcha_iframe")  # 切换到iframe DOM

    driver.find_element_by_id("reload").click()

    driver.switch_to.window(handle)
    return True


def _handle_img_xy():
    # 获取两张图片地址
    time.sleep(0.5)
    bg_img = driver.find_element_by_id("slideBg").get_attribute("src")
    front_img = driver.find_element_by_id("slideBlock").get_attribute("src")
    print("背景图片：{}\r\n{}".format(bg_img, front_img))

    # 计算出图片后缀
    img_index_and_sub_sid = _get_slider_subsid(bg_img)
    img_index = img_index_and_sub_sid[0]
    sub_sid = img_index_and_sub_sid[1]
    print("img_index={} sub_sid={}".format(img_index, sub_sid))

    # 生成图片本地地址
    t = _date()
    bg_img_path = _get_slider_img_bg_path(sub_sid, img_index, t)
    front_img_path = _get_slider_img_front_path(sub_sid, img_index, t)
    temp_img_path = _get_slider_img_temp_path(sub_sid, img_index, t)
    result_img_path = _get_slider_img_result_path(sub_sid, img_index, t)
    result_txt_path = _get_slider_txt_result_path(sub_sid, img_index, t)
    bg_img_src_path = _get_slider_txt_bg_path(sub_sid, img_index, t)
    print("保存地址：{}".format(bg_img_path))

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
    print("计算结果位置：x={}, y={}".format(x, y))

    # 保存x数据到txt
    file_handle = open(result_txt_path, 'w')
    file_handle.write("{}".format(x))

    # 保存bg src到txt
    file_handle = open(bg_img_src_path, 'w')
    file_handle.write(bg_img)

    result = {}
    result["xy"] = xy_array
    result["img_path"] = [bg_img_path, front_img_path, temp_img_path, result_img_path, result_txt_path, bg_img_src_path]
    return result


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


def _get_slider_img_bg_path(subsid, img_index, t):
    return "./img/slider/{}_{}_{}_bg.jpeg".format(subsid, img_index, t)


def _get_slider_img_front_path(subsid, img_index, t):
    return "./img/slider/{}_{}_{}_front.png".format(subsid, img_index, t)


def _get_slider_img_temp_path(subsid, img_index, t):
    return "./img/slider/{}_{}_{}_temp.png".format(subsid, img_index, t)


def _get_slider_img_result_path(subsid, img_index, t):
    return "./img/slider/{}_{}_{}_result.png".format(subsid, img_index, t)


def _get_slider_txt_result_path(subsid, img_index, t):
    return "./img/slider/{}_{}_{}_result.txt".format(subsid, img_index, t)


def _get_slider_txt_bg_path(subsid, img_index, t):
    return "./img/slider/{}_{}_{}_bg_src.txt".format(subsid, img_index, t)


def collect_data():
    return True


def main():
    click_search()

    # 判断状态，状态有三种，1、正常返回，2、验证码，3、频次限制
    if is_return_data():    # 判断是否返回数据
        collect_data()
        # continue

    if is_need_verify(5):    # 判断是否需要验证验证码
        for i in range(VERIFY_RETRY):
            xy_and_img_local_path = do_verify(i)
            time.sleep(2)
            if is_need_verify(1):
                print("第{}次验证失败，准备重试。".format(i))
                record_failed_img(xy_and_img_local_path)
                refresh_verify()
                time.sleep(2)
            else:
                print("第{}次验证成功。".format(i))
                break

    print("over")


def _date():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


if __name__ == "__main__":
    main()


# assert "no result found" not in driver.page_source
# driver.close()    # 关闭当前tab
# driver.quit()     # 关闭整个浏览器


