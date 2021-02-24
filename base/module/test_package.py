# 包
# 包就是一种管理python模块命名空间的形式。
# 某个目录下只有包含了一个叫__init__.py的文件才会被认作是一个包。

import traffic.car.suv as suv
import traffic.car.sedan as sedan
import traffic.plane.helicopter as co

suv.get_name()
sedan.get_name()
co.get_name()


