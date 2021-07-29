import math #导入math

a=int(input())
if(a==1):
    print('不是质数')
else:
    for i in range(2,int(math.sqrt(a))):   #折半查找
        if(a%i==0):
            flag=0 #利用bool变量防止输出过多
        else:
            flag=0

if(flag==0):
    print('不是质数')
else:
    print('是质数')
