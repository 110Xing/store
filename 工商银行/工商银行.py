import random
import pymysql
from DB import select
from DB import update

print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank_name="汉科软地球中国区老牛湾分行"#全局变量
bank={}#用户库

def bank_useradd(username,password,country,province,street,door,account,money):
    sql1="select count(*) from person"
    param1=[]
    data1= select (sql1,param1)
    if data1 [0][0]>= 100:
        return 3

    sql2="select * from person where account =%s"
    param2=[account]
    data2= select (sql2,param2)
    if len(data2) !=0:
        return 2

    sql3="insert into person values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
    param3=[account,username,password,country,province,street,door,money,bank_name]
    update(sql3,param3)

    return 1




def useradd():
    username=input("请输入您的用户名")
    password=int(input("请输入您的密码"))
    print("下面请您输入您的地址")
    country=input("\t\t请输入您所在的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    money=input("请输入您的存款金额")
    account=random.randint(10000000,99999999)
    status=bank_useradd(username,password,country,province,street,door,account,money)
    if status==1:

        print("恭喜你成功开户，以下是您的信息")
        info='''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
        
            '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, money, bank_name))
    elif status==2:
        print("该用户名已存在")
    elif status==3:
        print("恭喜你成功开户，以下是您的信息")
        info = '''
                            ------------个人信息------------
                            用户名:%s
                            账号：%s
                            密码：*****
                            国籍：%s
                            省份：%s
                            街道：%s
                            门牌号：%s
                            余额：%s
                            开户行名称：%s

                    '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, money, bank_name))
        print("注册用户已满")

def cq():
    account=int(input("请输入你的账号"))
    con = pymysql.connect(host="localhost", user="root", password="", database="gsyh")
    cursor = con.cursor()
    sql4 = "select * from person where account =%s"
    param4= [account]
    data4=cursor.execute(sql4,param4)

    if data4>0:
        data4_1 = cursor.fetchone()
        print(data4_1[7])
        cqm=int(input("请输入你的存款金额"))

        sql5="update person set money=money+%s where account=%s"
        param5 = [cqm,param4]
        cursor.execute(sql5,param5)
        con.commit()

        print("存款成功")
        sql6 = "select * from person where account =%s"
        cursor.execute(sql6,param4)
        data4_2 = cursor.fetchone()
        info = '''
                                        ------------个人信息------------
                                        账号：%s
                                        余额：%s
                                        开户行名称：%s
    
                                '''
        print(info % ( data4_2[0], data4_2[7], bank_name))
    else:
        print("输入账户不正确")
    cursor.close()
    con.close()

def qq():
    account=int(input("请输入你的账号"))
    password=int(input("请输入你的密码"))
    con = pymysql.connect(host="localhost", user="root", password="", database="gsyh")
    cursor = con.cursor()
    sql0 = "select * from person where account =%s and password =%s"
    param0 = [account,password]
    data0 = cursor.execute(sql0, param0)

    if data0>0:
        data=cursor.fetchone()
        print(data)
        qq=int(input("请输入你的取款金额"))
        sql1 = "update person set money=money-%s where account=%s"
        param1 = [qq, account]
        cursor.execute(sql1, param1)
        con.commit()
        print("取款成功")
        sql2 = "select * from person where account =%s "
        cursor.execute(sql2, account)
        data = cursor.fetchone()

        info = '''
                                                            ------------个人信息------------
                                                            账号：%s
                                                            余额：%s
                                                            开户行名称：%s
        
                                                    '''
        print(info % (data[0], data[7], bank_name))
        cursor.close()
        con.close()
    else:
        print("账户信息错误")



def zz():       #转账
    con = pymysql.connect(host="localhost", user="root", password="", database="company")
    cursor = con.cursor()
    while True:
        info = input("请输入转出账户：")
        sql1 = "select * from person where account = %s"
        info = [info]
        data = cursor.execute(sql1, info)
        if data > 0:
            while True:
                pwd = input("请输入密码")
                sql2 = "select password from person where password = %s and account = %s"
                pwd = [pwd,info]
                data = cursor.execute(sql2, pwd)
                if data > 0:
                    while True:
                        account = input("请输入转入账户：")
                        sql3 = "select account from person where account = %s"
                        fin = [account]
                        data = cursor.execute(sql3, fin)
                        if data > 0 :
                            while True:
                                money = input("请输入转账金额：")
                                if money.isdigit():
                                    sql4 = "select money from person where account = %s"
                                    cursor.execute(sql4, info)
                                    data = cursor.fetchone()
                                    if int(data[0]) < int(money):
                                        print("余额不足，转账失败！")
                                        continue
                                    else:
                                        money = int(money)
                                        sql5 = "update person set money=money - %s where account = %s"
                                        take = [money, info]
                                        cursor.execute(sql5,take)
                                        con.commit()
                                        sql6 = "update person set money=money + %s where account = %s"
                                        save = [money,fin]
                                        cursor.execute(sql6,save)

def cx():
    account = int(input("请输入你要查询的账号"))
    password = int(input("请输入你要查询账号的密码"))
    con = pymysql.connect(host="localhost", user="root", password="", database="gsyh")
    cursor = con.cursor()
    sql0 = "select * from person where account =%s and password =%s"
    param0 = [account, password]
    data0 = cursor.execute(sql0, param0)
    if data0>0:
        data=cursor.fetchone()
    info = '''
                                            ------------个人信息------------
                                            
                                            账号：%s
                                            密码：*****
                                            国籍：%s
                                            省份：%s
                                            街道：%s
                                            门牌号：%s
                                            余额：%s
                                            开户行名称：%s

                                    '''
    print(info % ( data[0], data[3], data[4], data[5], data[6],data[7], bank_name))
    cursor.close()
    con.close()


def tc():
    print("拜拜了你嘞")

while True:
    begin = input("请选择业务")
    if begin == "1":
        useradd()


    elif begin == "2":
        cq()

    elif begin == "3":
        qq()

    elif begin == "4":
        zz()
    elif begin == "5":
        cx()
    elif begin == "6":
        tc()
        break
    else:
        print("你瞎输入什么东西")
        break