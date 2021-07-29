arr=[]
while(True):  
    sign=input('是否继续输入（y/n）：')
    if(sign=='y'):
        arr.append(int(input()))
        continue
    elif(sign=='n'):
         break        #输入n停止
len=len(arr)          #总数
sum=0
for i in range(len):
    sum+=arr[i]       #总和
print(sum/len)        #平均值
