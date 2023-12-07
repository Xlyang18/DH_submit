# 定义汽车类
class Car:
    def run(self):
        print("汽车启动，开始行驶")

# 定义小汽车类，继承自汽车类
class SmallCar(Car):
    def stop(self):
        print("小汽车停止")

# 实例化一个汽车对象并调用 run() 方法
car = Car()
car.run()

# 实例化一个小汽车对象并调用 run() 和 stop() 方法
small_car = SmallCar()
small_car.run()
small_car.stop()
