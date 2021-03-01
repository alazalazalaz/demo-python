from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

timeout_sec = 12

driver = webdriver.Chrome()
driver.get("https://www.luckyair.net/flight/search.html")
# time.sleep(10)
# 等待可点击
# try:
#     element = WebDriverWait(driver, timeout_sec).until(
#         EC.presence_of_element_located((By.XPATH, "//input[@placeholder='出发城市']"))
#     )
# finally:
#     print("等待{}s后未发现元素\r\n".format(timeout_sec))
    # driver.quit()

assert "祥鹏" in driver.title         # 判断标题中是否含有Python，如果没有，则终止
# 出发
from_city_input = driver.find_element_by_xpath("//input[@placeholder='出发城市']")
from_city_input.clear()    # 清空input
from_city_input.send_keys("KMG")     # 输入pycon到input
time.sleep(0.5)
from_city_input.send_keys(Keys.RETURN)     # 回车

# 到达
to_city_input = driver.find_element_by_xpath("//input[@placeholder='到达城市']")
to_city_input.clear()    # 清空input
to_city_input.send_keys("CTU")     # 输入pycon到input
time.sleep(0.5)
to_city_input.send_keys(Keys.RETURN)     # 回车

# 搜索
search_button = driver.find_element_by_xpath("//button[@type='button']")
search_button.send_keys(Keys.RETURN)

# assert "no result found" not in driver.page_source
# driver.close()    # 关闭当前tab
# driver.quit()     # 关闭整个浏览器


