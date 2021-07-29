from random import randint        #引入随机整数函数

arr=[]                           #初始化数组
for i in range(20):
    arr.append(randint(1,100))    #读入数组
print('排序前的列表为：{}'.format(arr))
arr.sort()                              #排序

print('排序后的列表为：{}'.format(arr))
