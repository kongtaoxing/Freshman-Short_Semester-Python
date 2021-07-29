sum=0#初始化账本金额为0
while(True):
    print('请输入事件类型及金额！退出请输入n！')
    thing=input()
    if(thing=='C'): #取款
        num=int(input())
        sum-=num
    elif(thing=='S'):#取款
        num=int(input())
        sum+=num
    elif(thing=='n'):#结束
        break

print(sum)
