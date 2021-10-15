'''
需求：
3个厨师，造汉堡，每造一个向篮子扔一个，当篮子已经满的时候，停3秒，判断是否已满，没满，继续造汉堡

都有10000元，每个5元，6个人同时抢，当汉堡篮子不够，等3秒，判断是否还有，到钱花完为止

汉堡篮子，最多只能放500个
'''

from threading import Thread
import  time
kfc = 0
class cs(Thread):
    def run(self) -> None:
        global kfc
        while True:
            if kfc <= 500 and kfc >= 0:
                kfc = kfc + 1

            else:
                time.sleep(3)
                break
class gk(Thread):
    username = ""
    money = 10000
    count = 0
    def run(self) -> None:
        global kfc
        while True:
            if self.money > 0:
                kfc = kfc - 1
                self.money = self.money - 5
                self.count = self.count + 1
                print(self.username, "总共抢了", self.count, "个汉堡，剩余", self.money, "钱！")
                time.sleep(3)

            else:
                break
cs1 = cs()
cs2 = cs()
cs3 = cs()
gk1 = gk()
gk1.username = "老王"
gk2 = gk()
gk2.username = "老张"
gk3 = gk()
gk3.username = "老李"
gk4 = gk()
gk4.username = "老刘"
gk5 = gk()
gk5.username = "胖子"
gk6 = gk()
gk6.username = "旺财"

cs1.start()
cs2.start()
cs3.start()
gk1.start()
gk2.start()
gk3.start()
gk4.start()
gk5.start()
gk6.start()