gra=int(input())#输入成绩
#使用选择结构分类列举
if(gra>100):
    print('成绩高于100分，错误')
elif(gra>=90 and gra<=100):
    cj='A'
elif(gra>=80 and gra<90):
    cj='B'
elif(gra>=70 and gra<80):
    cj='C'
elif(gra>=60 and gra<70):
    cj='D'
elif(gra>=0 and gra<60):
    cj='E'
else:
    print('成绩低于0分，错误')

print(cj) #输出等级制成绩
