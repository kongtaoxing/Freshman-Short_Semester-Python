def f(n): 
    if(n<=1): 
        return n #前两项分类出去 
    else: 
        return f(n-1)+f(n-2) #递归调用 

n=int(input()) 
for i in range(n): 
    print(f(i),end=' ') #中间打上空格
