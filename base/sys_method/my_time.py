# time
import time
import calendar

# 当前时间戳
print(time.time())  # 1614175762.453156
print(int(time.time()))     # 1614175762

# 字符串转时间戳
date = "2020-08-08 01:01:01"
t = time.mktime(time.strptime(date, "%Y-%m-%d %H:%M:%S"))
print("字符串转时间戳 {}".format(int(t)))

# 时间戳转格式化字符串
timestamp = time.time() # 当前时间戳
date = time.localtime(timestamp)  # timestamp可以不传，默认为当前时间戳
# 2021-2-24 22:16:13
print("单独的 {}-{}-{} {}:{}:{}".format(date.tm_year, date.tm_mon, date.tm_mday, date.tm_hour, date.tm_min, date.tm_sec))
# 2021-02-24 22:19:58
# time.strftime()方法的分钟和秒是用大写的M和S，其他语言是i和s（Y-m-d H:i:s）
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取年月
print(time.strftime("%B", time.localtime()))
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

# print(calendar.month(2020, 2))

