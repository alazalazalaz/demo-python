import os
import sys


def file_path():
    print("我是second/my_sys2.py:{}".format(os.path.realpath(sys.argv[0])))
    print("我是second/my_sys2.py:{}".format(os.path.realpath(__file__)))
