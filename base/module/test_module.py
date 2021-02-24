import log
from log import log_info as info

# 使用import引用模块
log.log_info("这个是info")
log.log_error("这个是error")
# from import引入部分
info("from引入的info")

print(dir(log))
