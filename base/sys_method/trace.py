import traceback


def func():
    raise Exception("im a exception")


def main():
    try:
        func()
    except Exception as e:
        print("捕获异常:{}".format(e)) # 捕获异常:im a exception
        print("trace route:{} ".format(traceback.print_exc())) #输出trace route如下
        """
        Traceback (most recent call last):
          File "trace.py", line 10, in main
            func()
          File "trace.py", line 5, in func
            raise Exception("im a exception")
        Exception: im a exception
        trace route:None 
        """

    print("xxxxx")

main()
