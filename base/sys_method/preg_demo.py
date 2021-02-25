# preg 实例

import re
print("=================== phone ================")
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

print("=================== mail ================")
# 匹配邮箱
email_preg = re.compile("^\w+@\w+\.\w+$")
email = "xxx@qq.com"
email1 = "222qq.com"
email2 = "xxx@qqcom"
email3 = "232esdfj*@qq.com"
print(email_preg.search(email))     # <re.Match object; span=(0, 10), match='xxx@qq.com'>
print(email_preg.search(email1))    # None
print(email_preg.search(email2))    # None
print(email_preg.search(email3))    # None

print("=================== html中的图片地址 ================")
# 匹配html中的图片地址
content = """
<div class="m-error" id="j-error">
<a href="http://you.163.com/flashSale/index?from=web_rk_mail_rc_0&amp;_stat_subject=5743" target="_blank" data-psc-stat="8d676c3f48e2a9b14514abaea8503a30"></a> 
<img src="https://yanxuan.nosdn.127.net/test.jpg">
</div>
<div class="m-error" id="j-error">
<a href="http://you.163.com/flashSale/index?from=web_rk_mail_rc_0&amp;_stat_subject=5743" target="_blank" data-psc-stat="8d676c3f48e2a9b14514abaea8503a30"></a> 
<img src="https://yanxuan.nosdn.127.net/15245672170585511.jpg">
</div>
"""
content_preg = re.compile("<img src=\"(.*)\">")
content_result = content_preg.findall(content)
print(content_result)   # ['https://yanxuan.nosdn.127.net/test.jpg', 'https://yanxuan.nosdn.127.net/15245672170585511.jpg']
