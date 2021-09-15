#实现输入10个数字，并打印10个数的求和结果
import random
ran=random.randint(0,10)
a=500
c=1
while True :
    print("你的余额为：", a)
    b=int(input("请输入一个数字"))
    if b==ran:
        print("OK")
        a=a+10
        ran=random.randint(0,10)
    elif c==3:
        print("你的余额为：",a)
        print("你猜错了")
        break
    else:
        a=a-100
        print("你猜错了")
        c=c+1

