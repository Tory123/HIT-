import os
import collections
from collections import Counter

f = open("test2.txt")
r = open("out.txt",'w')
p = open("wordout.txt",'w')
data = f.readlines()
#print(data[0][23:])
#for i in range(len(data)):
#    r.write(data[i][23:])
#提取不同词性的词，策略是遍历所有词，依次判断词性，放入对应的列表
 #定义列表
#名词
n = list()
#动词
v = list()
#数词
m = list()
#形容词
a = list()
#副词
d = list()
#时间词
t = list()
#成语
ic = list()
#助词
u = list()
#介词
p = list()
#连词
c = list()
#形语素
Ag = list()
#副形词
ad = list()
#名形词
an = list()
#区别语素
Bg = list()
#区别词
b = list()
#副语素
Dg = list()
#叹词
e = list()
#方位词
f = list()
#语素
g = list()
#前接成分
h = list()
#简略语
ji = list()
#后接成分
k = list()
#数语素
Mg = list()
#名语速
Ng = list()
#人名
nr = list()
#地名
ns = list()
#拟声词
o = list()
#机构团体
nt = list()
#外文字符
nx = list()
#其他专名
nz = list()
#量语速
Qg = list()
#量词
q = list()
#代语素
Rg = list()
#代词
r = list()
#处所词
s = list()
#时间语素
Tg = list()
#时间词
t = list()
#助语素
Ug = list()
#助词
u = list()
#动语素
Vg = list()
#副动词
vd = list()
#名动词
vn = list()
#标点符号
w = list()
#非语素字
x = list()
#语气语素
Yg = list()
#语气词
y = list()
#状态词
z = list()

#s = (data[0][23:].split())[0]
#print(s[s.rfind('/', 1) + 1])
l = list()
for i in range(len(data)):
   l = data[i][23:].split()
   for j in range(len(l)):
       if  ( l[j][l[j].rfind('/', 1) + 1:]=="n"): n.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="v"): v.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="m"): m.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="a"): a.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="d"): d.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="t"): t.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="i"): ic.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="u"): u.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="p"): p.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="c"): c.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="Ag"): Ag.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="ad"): ad.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="an"): an.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="Bg"): Bg.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="b"): b.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="Dg"): Dg.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="e"): e.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="f"): f.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="g"): g.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="h"): h.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="j"): ji.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="k"): k.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="Mg"): Mg.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="Ng"): Ng.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="nr"): nr.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="ns"): ns.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="o"): o.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="nt"): nt.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="nx"): nx.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="nz"): nz.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="Qg"): Qg.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="q"): q.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="Rg"): Rg.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="r"): r.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="s"): s.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="Tg"): Tg.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="t"): t.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="Ug"): Ug.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="u"):  u.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="Vg"): Vg.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="vd"): vd.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="vn"): vn.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="w"): w.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="x"): x.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="Yg"): Yg.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="y"): y.append(l[j])
       elif( l[j][l[j].rfind('/', 1) + 1:]=="z"): z.append(l[j])
print("名词个数为：")
print(len(n))
print("动词个数为：")
print(len(v))
print("形容词个数为：")
print(len(a))
print("数词个数为：")
print(len(m))
print("副词个数为：")
print(len(d))
print("时间词个数为：")
print(len(t))
print("成语个数为：")
print(len(ic)) 
print("助词个数为：")
print(len(u)) 
print("介词个数为：")
print(len(p))
print("连词个数为：")
print(len(c))
print("形语素个数为：")
print(len(Ag))
print("副形词个数为：")
print(len(ad))
print("名形词个数为：")
print(len(an))
print("#区别语素个数为：")
print(len(Bg))
print("区别词个数为：")
print(len(b))
print("副语素个数为：")
print(len(Dg))
print("叹词个数为：")
print(len(e))
print("方位词个数为：")
print(len(f))
print("语素个数为：")
print(len(g))
print("前接成分个数为：")
print(len(h))
print("简略语个数为：")
print(len(ji))
print("后接成分个数为：")
print(len(k))
print("数语素个数为：")
print(len(Mg))
print("名语速个数为：")
print(len(Ng))
print("人名个数为：")
print(len(nr))
print("地名个数为：")
print(len(ns))
print("拟声词个数为：")
print(len(o))
print("机构团体个数为：")
print(len(nt))
print("外文字符个数为：")
print(len(nx))
print("其他专名个数为：")
print(len(nz))
print("量语素个数为：")
print(len(Qg))
print("量词个数为：")
print(len(q))
print("代语素个数为：")
print(len(Rg))
print("量语素个数为：")
print(len(Qg))
print("代词个数为：")
print(len(r))
print("处所词个数为：")
print(len(s))
print("时间语素个数为：")
print(len(Tg))
print("时间词个数为：")
print(len(t))
print("助语素个数为：")
print(len(Ug))
print("助词个数为：")
print(len(u))
print("助词个数为：")
print(len(u))
print("动语素个数为：")
print(len(Vg))
print("副动词个数为：")
print(len(vd))
print("名动词个数为：")
print(len(vn))
print("标点符号个数为：")
print(len(w))
print("非语素字个数为：")
print(len(x))
print("语气语素个数为：")
print(len(Yg))
print("语气词个数为：")
print(len(y))
print("状态词个数为：")
print(len(z))

#找出十个频率最高的词
longlist = list()
for i in range(len(data)):
   l = data[i][23:].split()
   for j in range(len(l)):
      longlist.append(l[j])
all_dic = collections.Counter(longlist)
top_ten = all_dic.most_common(10)
#print(top_ten)
#名词统计
n_dic = collections.Counter(n)
n_top_ten = n_dic.most_common(10)
print(n_top_ten)
#ctr =  collections.Counter(n)
#print(ctr)
#将所有词存入列表，collections.Counter转化为词典，统计出现频率

#    for j in (data[i][23:].split()) 
#        print ((data[i][23:].split()) [j].rfind('\') ) 
                      # noun.append(data[i][23:].split()) [j])
                      # print("123")
#print(len(data))
#print list.count(data)
