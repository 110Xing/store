c=0#次数
while True :
    a=str(input("请输入用户名："))
    b=str(input("请输入用户名密码："))

    if a=="root"and b=="admin":
        print("输入用户名和密码正确")
        break
    else:
        print("输入用户名和密码不正确")
        c=c+1
        if c==3:
            print("次数已用尽")
            break
