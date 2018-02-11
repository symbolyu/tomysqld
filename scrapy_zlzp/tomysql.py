# coding=utf-8
import pymysql
import MySQLdb
import json

# 将json内容导入数据库
salary = []
name = []
f = open("F:/python/items8.json")
s = json.load(f)


# s[0]['name']是一个list 没有decode方法
# 讲list转Unicode
for i in range(len(s)):
    a = "".join(s[i]['name'])
    b = "".join(s[i]['salary'])
    s_u1 = a
    s_u2 = b
    s_str1 = s_u1.encode('unicode-escape').decode('string_escape')
    s_str2 = s_u2.encode('unicode-escape').decode('string_escape')
    name.append(s_str1)
    salary.append(s_str2)

# 判断是否存在
for a in range(len(name)):
    if(name[a]):
        pass
    else:
        name[a] = "none"
    if(salary[a]):
        pass
    else:
        salary[a] = "none"

t1 = []
t2 = []
str1 = ""
str2 = ""
# 将unicode转中文
for y in range(len(name)):
    str1 = name[y].decode('unicode-escape')
    t1.append(str1)
    str2 = salary[y].decode('unicode-escape')
    t2.append(str2)



# #传入数据库
conn = MySQLdb.connect(host='localhost',user='root',passwd='123',db='test',charset='utf8')
cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
for i in range(len(t1)):
    sql = 'insert into scrapy_python values(%s,%s)'
    arg = (t1[i].encode('utf-8'),t2[i].encode('utf-8'))
    r = cur.execute(sql,arg)
nRet = cur.fetchall()
conn.commit()
cur.close()
conn.close()
print "ok"

