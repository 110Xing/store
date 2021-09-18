a=int(input("输入一个数字："))
b=int(input("输入一个数字："))
c=int(input("输入一个数字："))
if a<b+c and b<a+c and c<a+b:
    if a==b and b==c:
         print("等边三角形")
    elif a==b or b==c or a==c:
        if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            print ("等腰直角三角形")
        else:
            print("等腰三角形")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("直角三角形")
    else:
        print("普通三角形")
else:
    print("无法构成三角形")



