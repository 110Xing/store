'''
    进程：
    正在运行的程序

    多线程：
    python:
    Thread体系类完成多线程的功能
    1.子类继承Tread类
    2.重写run方法：写任务代码
    3.启动，并执行。start（）

'''
from  threading import  Thread
class PCmanager(Thread):

    def run(self) -> None:
        #杀毒的任务程序
        for i in range(10000):
            print("电脑管家真在杀毒，已经杀了",i,"个毒")

class PC360(Thread):
    def run(self) -> None:
        for i in range(10000):
            print("360管家真在杀毒，已经杀了", i, "个毒")

p1 = PC360()
p2 = PCmanager()

p1.start()
p2.start()


'''
需求：
抢票：
    500张票
    刘备，关羽，张飞。抢票，抢到谁算谁的。看谁抢的多:
'''
from  threading import Thread
ticket = 500
class Person(Thread):
    username = ""
    count = 0

    def run(self) -> None:
        global ticket  #声明使用全局变量
        while True:
            if ticket > 0 :
                self.count = self.count + 1
                ticket = ticket-1
                print("嘻嘻！",self.username,"我成功抢到了一张票，还剩",ticket,"票！")
            else:
                print(self.username,"总共抢了",self.count,"张票！")
                break
p1 = Person()
p1.username = "刘备"
p2 = Person()
p2.username = "张飞"
p3 = Person()
p3.username = "关羽"

p1.start()
p2.start()
p3.start()



















