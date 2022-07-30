#!/usr/Yan/VSscripts
# Filename: WorkBook.py
# Description: Some exercises for python coding.

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#count=0
#for i in (1,2,3,4):
    #for j in (1,2,3,4):
        #for k in (1,2,3,4):
            #if i!=j and j!=k and k!=i:
                #print('The inclusive answer is', i*100+j*10+k)
                #count+=1
#print('Total:', count)
ans=[]
count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and k!=i:
                ans.append(i*100+j*10+k)
                count+=1
print('Total:', count, 'Answers:', ans)

#企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
#I=int(input('请输入当月利润：'))
#if I<=10:
#    bon=I*0.1
#elif I>10 and I<=20:
#    bon=1+(I-10)*0.075
#elif I>20 and I<=40:
#    bon=1+0.75+(I-20)*0.05
#elif I>40 and I<=60:
#    bon=1+0.75+1+(I-40)*0.03
#elif I>60 and I<=100:
#    bon=1+0.75+1+0.6+(I-60)*0.015
#else:
#    bon=1+0.75+1+0.6+0.6+(I-100)*0.01
#print('发放的奖金是：', bon, '万元')

# OR
I = int(input('Enter the profit:'))
cas = [100,60,40,20,10,0]
rate = [0.01,0.015,0.03,0.05,0.075,0.1]
bon = 0
for idx in range(0,6):
    if I>cas[idx]:
        bon+=(I-cas[idx])*rate[idx]
        I=cas[idx]
print ('The bonus is (ten thausand): ', bon)

#一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
#转换成：有两个能被开方的数，一个比另一个高168
cel=2
anw=[]
while cel**2-(cel-1)**2<168:
    #print(cel**2-(cel-1)**2, cel)
    cel+=1
for i in range(1, cel+1):
    for j in range(1, i):
        if i**2-j**2==168:
            anw.append(j**2-100)
print('Over!', 'The anwsers contain:', anw)

#或（但这样不好，没有考虑到多个答案以及小于0的情况-取决于num的起点取值）
import math

num = 1000
while True:
    if math.sqrt(num + 100)-int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 268)-int(math.sqrt(num + 268)) == 0:
        #print(num)
        break
    num += 1
print('The anwser could be:', num)

#输入某年某月某日，判断这一天是这一年的第几天？
year=int(input('Please input the current year:'))
mon=int(input('Please input the current month:'))
day=int(input('Please input the date today:'))
Cmon=[12,11,10,9,8,7,6,5,4,3,2,1]
Cday=[31,30,31,30,31,31,30,31,30,31,29 if year%4==0 else 28,31]
for i in range(12):
    if mon==Cmon[i]:
        No=day+sum(Cday[i+1:12])
        print('No.', No, 'days')
        break

#输入三个整数x,y,z，请把这三个数由小到大输出。(还可用冒泡算法)
#a,b = map(lambda x:int(x),input("请输入两个数：").split())
x,y,z=eval(input("请输入3个整数，中间用逗号','分开："))
ord=[]
if x>=y and x>=z:
    ord.append(x)
    if y>=z:
        ord.append(y)
        ord.append(z)
    else:
        ord.append(z)
        ord.append(y)
elif y>x and y>=z:
    ord.append(y)
    if x>=z:
        ord.append(x)
        ord.append(z)
    else:
        ord.append(z)
        ord.append(x)
else:
    ord.append(z)
    if x>=y:
        ord.append(x)
        ord.append(y)
    else:
        ord.append(y)
        ord.append(x)
print('The order is:', ord)

#输出9*9口诀
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,)
    print('')

#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？(斐波那契数列)
#以20个月为例
a=0
b=1
for i in range(2,21):
    c=b
    b=a+b
    a=c
    print('第', i, '个月兔子总数为', b)
    i+=1
#或
a = 1
b = 1
for i in range(1,21,2):
    print('%d %d'%(a,b))
    a += b
    b += a

#判断101-200之间有多少个素数，并输出所有素数
num=[]
cont=0
import math as m
for i in range(101,201):
    k=int(m.sqrt(i))+1
    lab=0
    for j in range(2,k):
        if i%j==0:
            lab=1
            break
    if lab==0:
        num.append(i)
        cont+=1
print('Number of sushu:', cont, 'sushu:', num)

#打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方
def main():
    for i in range(100,1000):
        a=int(i/100)
        b=int((i-a*100)/10)
        c=i%10
        if i==a**3+b**3+c**3:
            print(i, '是一个水仙花数')
if __name__=='__main__':
    main()

#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
s=input('please input any string here:')
letter=0
digit=0
space=0
other=0
for c in s:
    if c.isalpha():
        letter+=1
    elif c.isdigit():
        digit+=1
    elif c.isspace():
        space+=1
    else:
        other+=1
print(letter, digit, space, other)

#打印出如下图案（菱形）
for i in range(1,5):
    print(' '*(4-i)+'*'*(2*i-1))
for i in range(5,8):
    print(' '*(i-4)+'*'*(15-2*i))

#利用递归方法求5!
def fun(i):
    if i==1:
        return 1
    return i*fun(i-1)

fun(5)

#利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
def rev(s,l):
    if l==0:
        return
    print(s[l-1])
    rev(s,l-1)
s=input('Please input a string:')
rev(s,len(s))

#画圆
if __name__ == '__main__':
    from tkinter import *

    canvas = Canvas(width=800, height=600, bg='green')  
    canvas.pack(expand=YES, fill=BOTH)                
    k = 1
    j = 1
    for i in range(0,26):
        canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1)
        k += j
        j += 0.3

    mainloop()

#模拟Linux用户登录。验证账号和密码，若失败则延迟三秒输出错误信息。
import time

global user, name

user = {
    'woider': '3243',
}


def login():
    global name
    name = input('Username:')
    pswd = input('Password:')
    if name not in user:
        return False
    return user[name] == pswd


while (not login()):
    time.sleep(3)  # 暂停3秒
    print('Authentication failure')

print(name + '@localhost:~$')

#格式化输出当前时间。使用 time 模块，格式为 yyyy-mm-dd HH:mm:ss

import time

format = '%Y-%m-%d %H:%M:%S'
local = time.localtime(time.time())
print(time.strftime(format, local))


# Test list
a=[1,2,3,'2']
print(a)
a.append(0)
a.clear()
a[0]=1
a=[2,6,4,5,7,32,1]
a.sort()


# Challenge 1 - string translate
raw="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(''.join([chr(((ord(s) + 2) - ord('a')) % 26 + ord('a')) if s >= 'a' and s <= 'z' else s for s in raw]))


table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
result = raw.translate(table)
print(result)

# Challenge 2 - read html and count string
import urllib.request
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

import re
comments = re.findall("<!--(.*?)-->", html, re.DOTALL)
data=comments[-1]
count = {}
for c in data:
    count[c] = count.get(c, 0) + 1
# type(count)
print(count)
print("".join(re.findall("[A-Za-z]", data)))

# challenge 3 - find pattern in string
import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
data = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))


# 4 - loop of website
import requests
import re
web='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
name=eval('8022')

while True:
    cont=requests.get(web % name).text
    print(cont)
    match=re.search(r"(\d+)", cont)
    if match==None:
        break
    name=match.group(1)









