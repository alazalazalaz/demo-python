# preg 实例

import re

# 匹配正确的手机号
phone = "13612345678"
phone1 = "1234"
phone2 = "31312345678"
phone3 = "1234567856789456"
phone_preg = re.compile("^1\d{10}$")
print(phone_preg.search(phone))     # <re.Match object; span=(0, 11), match='13612345678'>
print(phone_preg.search(phone1))    # None
print(phone_preg.search(phone2))    # None
print(phone_preg.search(phone3))    # None

# 匹配邮箱 @todo