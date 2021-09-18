a=0#输入个数
b=0#和
c=b/10#和平均数
y=0
while True:
    d=int(input("请输入一个数字"))
    a=a+1
    b=b+d
    if y <  d:
        y = d
    if a==10:
        c=b/10
        print("和是：",b)
        print("和平均数是：",c)
        print("最大值是：",y)
        break
