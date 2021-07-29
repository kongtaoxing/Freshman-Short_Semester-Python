print('要输入整数的个数为：')
num=int(input())
print('选中最后多少个数字：')
choice=int(input())
arr=[]#初始化数组
for i in range(1,num+1):
    print('输入第{}/{}数字：'.format(i,num))
    arr.append(int(input())) #读入数据
print('原始列表{}'.format(arr))
arr=arr[num-choice:]+arr[:num-choice]#使用切片输出列表
print('移动之后：{}'.format(arr))
