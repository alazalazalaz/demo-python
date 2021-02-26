import traceback


def func():
    raise Exception("im a exception")


def main():
    try:
        func()
    except Exception as e:
        print("捕获异常:{}".format(e))
        print("trace route:{} ".format(traceback.print_exc()))


main()
