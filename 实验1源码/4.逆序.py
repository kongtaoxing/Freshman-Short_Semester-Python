a=input('请输入一个小于10位数的正整数')
arr=list(a)#分开各位数
arr.reverse()#逆序
b=len(arr)
print('这个数的长度是{}，逆序输出的结果是{}'.format(b,arr))
