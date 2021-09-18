a=0#输入个数
c=0#和
while True:
    b=int(input("请输入一个数字"))
    a=a+1
    c=c+b
    if a==10:
        print("和是：",c)
        break


