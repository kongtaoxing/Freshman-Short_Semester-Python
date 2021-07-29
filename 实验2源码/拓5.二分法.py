print('输入有序数组：',end='')
arr=list(map(int, input().split())) #输入数组
print('输入要查找的数字：',end='')
num=int(input())
left=0
right=len(arr)-1
while(left<=right):
    mid=(left+right)//2   #整除
    if(arr[mid]==num):
        print(mid)
        break             #输出后退出
    elif(arr[mid]>num):
        right=mid
    else:
        left=mid
