import log # 导入log.py整个模块
from log import log_info as info # 导入log.py中的log_info方法并命别名info

# 使用import引用模块
log.log_info("这个是info")
log.log_error("这个是error")
# from import引入部分
info("from引入的info")

print(dir(log))
