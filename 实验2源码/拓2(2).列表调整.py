arr=['cat','pig','dog','cattle','sheep','pig'] #初始化数组 
while 'pig' in arr: 
    arr.remove('pig') #删除所有pig 
with open("C:/Users/Hasee/Desktop/test.txt",'w') as fp: #打开文件 
    for i in range(4): 
        fp.write(arr[i]) 
        fp.write('\n') #读入数据并换行 
    fp.write('文件修改已完成！')
