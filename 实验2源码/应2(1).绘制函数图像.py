import csv #导入CSV模块
fp=open('附件3.csv') #打开文件
static=csv.reader(fp) 
string=[]
x0=[]
y0=[]
for row in static:
    string.append(str(row))
for i in range(5):
    x0.append(string[i+1][2])  #将x导入x0数组
    y0.append(string[i+1][9])  #将y导入y0数组
print(x0)
print(y0)
