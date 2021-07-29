up,low,digit,special=0,0,0,0 #分别定义flag变量
passwd=input('Please input your password:') #输入密码
if len(passwd)<6:
    print('weak')      #少于六个字符输出weak
else:
    string=list(passwd)
    for i in string:
        if 'A'<=i<='Z':
            up+=1
        elif 'a'<=i<='z':
            low+=1
        elif '0'<=i<='9':
            digit+=1
        elif i in ',.!:?<>':
            special+=1             #对flag变量进行判断

    judge=list(map(str,[up,low,digit,special])) #将数字装进列表中
    num=0#另一个flag变量，检查0的个数
    for i in judge:
        if i=='0':
            num+=1
    if num==2:
        print('below middle')
    elif num==1:
        print('above middle')
    elif num==0:
        print('strong')
