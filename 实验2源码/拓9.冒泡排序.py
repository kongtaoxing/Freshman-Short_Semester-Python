import random  #导入random模块

arr=[]
len=random.randint(1,20)
for num in range(len):    #随机元素数量的列表
    arr.append(random.randint(1,100)) #元素随机
print('排序之前的随机数列表为：{}'.format(arr))

for i in range(len):
    for j in range(i+1,len):
        if arr[i]>=arr[j]:
            (arr[i],arr[j])=(arr[j],arr[i])  #冒泡

print('排序之后的随机数列表为：{}'.format(arr))
