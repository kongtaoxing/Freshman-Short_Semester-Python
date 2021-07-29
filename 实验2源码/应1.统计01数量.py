data=[]
data_cope=[]
output=[]
with open('val_gt.txt','r') as fp:
    data_raw=fp.readlines()     #未经处理的数据
    for line in data_raw:
        data.append(line.split())
num1=0
num0=0
for i in range(9675):  
    for j in data[i]:
        if j=='1':
            num1+=1           #计算1的数量
        elif j=='0':
            num0+=1           #计算0的数量
    data_cope.append(data[i][0])
    data_cope[i]+=' '
    data_cope[i]+=str(num1)
    data_cope[i]+=' '
    data_cope[i]+=str(num0)   #将0和1 的数量添加到输出字符串结尾
    output.append(data_cope[i])
    num1=0                    
    num0=0                    #将num1和num0归零

with open('val_result.txt','w') as fp1:
    for i in range(9675):
        fp1.write(output[i])
        fp1.write('\n')       #写入文件
    
