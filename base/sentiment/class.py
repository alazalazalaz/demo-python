# class详解

# 定义
class Car:
    # public 成员
    name = ""
    price = 0
    # private 成员，private方法同理 __func()
    __weight = 0

    def __init__(self):     # 构造函数，实例化的时候会自动调用
        self.name = "car"
        print("我的父类的构造")

    def __del__(self):
        print("我是父类的析构")

    def get_name(self):     # 类方法和普通方法的唯一区别是类方法有一个额外的第一个参数名称，按照惯例叫self，表示的是实例本身
        print("父类的name={}".format(self.name))

    def get_price(self):
        print("父类的price={}".format(self.price))


car1 = Car()
print(car1.get_name())
print("=============")


# 继承
class Sedan(Car):
    name = "sedan"  # 此处的成员变量name和price不会自动覆盖掉父类的哦！！！
    price = 20

    def __init__(self):
        Car.__init__(self)  # 父类构造函数需要手动执行，否则不会执行
        print("我的子类的构造")

    def __del__(self):
        print("我是子类的析构")

    def get_price(self):
        print("子类的price={}".format(self.price))

    def get_name(self):
        print("子类的name={}".format(self.name))


sedan1 = Sedan()
sedan1.get_name()    # car 此处的成员变量name sedan不会自动覆盖父类的成员变量name car
sedan1.get_price()  # 20 price在父类初始值为0，构造函数中未被修改，所以会被自动覆盖为20

