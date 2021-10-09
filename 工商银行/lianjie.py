import pymysql
con =pymysql.connect(host="localhost",user="root",password="",database="gsyh")
cursor = con.cursor()
sql="insert into person values('s002','张三','123456','美国','纽约','s002','s002','950252','09点50分','中国工商银行')"

cursor.execute(sql)

con.commit()

cursor.close()
con.close()