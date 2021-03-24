import time
import re


def stringdhm2seconds(my_str):
    """把xxdxxhxxm格式转为秒"""
    result = re.search(r'(\d*)[d\s]*(\d*)[h\s]*(\d*)m', my_str)
    if result:
        d, h, m = 0, 0, 0
        if result.group(2) == "" and result.group(3) == "":
            m = int(result.group(3))
        elif result.group(2) == "":
            h = int(result.group(1))
            m = int(result.group(3))
        else:
            d = int(result.group(1))
            h = int(result.group(2))
            m = int(result.group(3))
        total = d * 86400 + h * 3600 + m * 60
        return total

if __name__ == "__main__":
    print(stringdhm2seconds("1h 11m"))
