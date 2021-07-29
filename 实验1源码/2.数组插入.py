print('请输入要插入的数字',end='')
num=int(input()) 
x=[1,10,30,40,60,100,200,900,num]
for k in range(0,8):
    if num>x[k]:
        m=k+1 
for i in range(0, 9):
    for j in range(0,9-i-1):
        if x[j]>x[j+1]:
            (x[j],x[j+1])=(x[j+1],x[j])
print('插入位置为',end='')
print(m,end='') 
print('，插入后的数组值为',end='')
print(x) 
