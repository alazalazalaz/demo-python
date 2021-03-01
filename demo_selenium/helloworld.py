from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title         # 判断标题中是否含有Python，如果没有，则终止
elem = driver.find_element_by_name("q")     # 获取name='q'的元素，这里是个Input
elem.clear()    # 清空input
elem.send_keys("pycon")     # 输入pycon到input
elem.send_keys(Keys.RETURN)     # 回车
assert "no result found" not in driver.page_source
# driver.close()    # 关闭当前tab
# driver.quit()     # 关闭整个浏览器


