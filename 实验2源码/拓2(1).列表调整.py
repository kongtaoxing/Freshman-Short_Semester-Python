arr=['cat','pig','dog','cattle','sheep','pig'] #初始化数组
with open("C:/Users/Hasee/Desktop/test.txt",'w') as fp:  #打开文件
    for i in range(6):
        fp.write(arr[i])
        fp.write('\n')    #读入数据并换行
    fp.write('文件写入已完成！')
