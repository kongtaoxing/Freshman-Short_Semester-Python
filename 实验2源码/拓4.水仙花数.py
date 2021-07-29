for i in range(100,1000):
    arr=map(int,str(i))#分开各位数
    arr=list(arr)      #map之后不能添加下标
    if(arr[0]**3+arr[1]**3+arr[2]**3==int(i)):
           print(i)
