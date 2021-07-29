import cmath #导入cmath
import math  #导入math

a=float(input())
b=float(input())
c=float(input()) #输入a,b,c
d=b**2-4*a*c #计算delta
if(d<0):
    print('有一对共轭虚根：',end='')
    print((-b-cmath.sqrt(d))/(2*a))
    print((-b+cmath.sqrt(d))/(2*a))
elif(d==0):
    print('有两相等实根：',end='')
    print((-b)/(2*a))
else:
    print('有二不等实根：',end='')
    print((-b-math.sqrt(d))/(2*a))
    print((-b+math.sqrt(d))/(2*a))
